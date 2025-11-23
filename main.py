import logging
import random
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler

# ======================= CONFIG =======================
BOT_TOKEN = "8538557025:AAHxyGoWwPnjnMIXzwngx8_CZQMBz9yM0Eg"
ADMIN_IDS = [6059547931]

# Railway environment variables
PORT = int(os.environ.get('PORT', 8080))
WEBHOOK_URL = os.environ.get('RAILWAY_STATIC_URL', '')

# ======================= VOCAB =======================
import logging
import random
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler

# ======================= CONFIG =======================
BOT_TOKEN = "8538557025:AAHxyGoWwPnjnMIXzwngx8_CZQMBz9yM0Eg"
ADMIN_IDS = [6059547931]

# Railway environment variables
PORT = int(os.environ.get('PORT', 8080))
WEBHOOK_URL = os.environ.get('RAILWAY_STATIC_URL', '')

# ======================= VOCAB =======================
vocab = {
    "1": {
        "afraid": "qo'rqmoq",
        "agree": "rozi bo'lmoq", 
        # ... sizning barcha unitlaringiz ...
    }
    # ... 30-gacha unitlar ...
}

# ======================= LOGGING =======================
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

active_tests = {}
user_answers = {}

def generate_question(unit_data):
    word, meaning = random.choice(list(unit_data.items()))
    correct = meaning
    wrong_options = [v for k, v in unit_data.items() if v != correct]
    wrongs = random.sample(wrong_options, min(3, len(wrong_options)))
    options = wrongs + [correct]
    random.shuffle(options)
    return word, correct, options

def get_keyboard(options):
    keyboard = [[InlineKeyboardButton(opt, callback_data=opt)] for opt in options]
    return InlineKeyboardMarkup(keyboard)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "😁 Salom! Men Vocabulary Bot man.\n"
        "Menda 30 ta unit bor!\n"
        "Meni guruhga qo'shing va admin qiling — shunda testlar ishlaydi 🚀"
    )

async def unit_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id

    if user_id not in ADMIN_IDS:
        await update.message.reply_text("❌ Faqat admin test boshlashi mumkin!")
        return

    if not context.args:
        await update.message.reply_text("Unit raqamini kiriting. Misol: /unit 7")
        return

    unit_num = context.args[0]
    if unit_num not in vocab:
        await update.message.reply_text(f"Unit {unit_num} mavjud emas! Faqat 1-30 unitlar mavjud.")
        return

    unit_data = vocab[unit_num]
    questions = []
    for _ in range(20):
        word, correct, options = generate_question(unit_data)
        questions.append({"word": word, "correct": correct, "options": options})

    active_tests[chat_id] = {
        "unit": unit_num,
        "questions": questions,
        "index": 0,
        "scores": {}
    }
    
    user_answers[chat_id] = {}

    await update.message.reply_text(
        f"🎲 'Unit {unit_num}' testiga tayyorlaning!\n"
        "🖊 20 ta savol\n\n"
        "Test boshlandi!"
    )
    
    await send_question(chat_id, context)

async def send_question(chat_id, context: ContextTypes.DEFAULT_TYPE):
    test = active_tests.get(chat_id)
    if not test:
        return
        
    idx = test["index"]
    if idx >= len(test["questions"]):
        # Test yakunlandi
        scores = test["scores"]
        leaderboard = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        msg = f"🏁 Unit {test['unit']} testi yakunlandi!\n20 ta savol berildi.\n\n"
        medals = ["🥇", "🥈", "🥉"]
        
        for i, (user_id, score) in enumerate(leaderboard[:3]):
            try:
                user = await context.bot.get_chat(user_id)
                user_name = user.first_name or f"User {user_id}"
            except:
                user_name = f"User {user_id}"
            msg += f"{medals[i] if i < 3 else '   '} {user_name} – {score}/20\n"
        
        if not leaderboard:
            msg += "Hech kim javob bermadi 😔"
        
        await context.bot.send_message(chat_id, msg)
        active_tests.pop(chat_id, None)
        user_answers.pop(chat_id, None)
        return

    question = test["questions"][idx]
    keyboard = get_keyboard(question["options"])
    message = await context.bot.send_message(
        chat_id, 
        f"❓ {question['word']} so'zining ma'nosini toping:\n\nSavol {idx + 1}/20", 
        reply_markup=keyboard
    )
    
    user_answers[chat_id][message.message_id] = {}

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id
    chat_id = query.message.chat.id
    message_id = query.message.message_id
    
    await query.answer()
    
    test = active_tests.get(chat_id)
    if not test:
        await query.edit_message_text("Test tugadi.")
        return

    idx = test["index"]
    question = test["questions"][idx]

    # User allaqachon javob berganmi tekshirish
    if user_answers.get(chat_id, {}).get(message_id, {}).get(user_id):
        await query.answer("Siz allaqachon javob berdingiz!", show_alert=True)
        return

    selected = query.data
    correct = question["correct"]

    # Score update
    if user_id not in test["scores"]:
        test["scores"][user_id] = 0
        
    if selected == correct:
        test["scores"][user_id] += 1
        await query.answer("✅ To'g'ri!")
    else:
        await query.answer("❌ Noto'g'ri!")

    # User javobini saqlash
    if chat_id not in user_answers:
        user_answers[chat_id] = {}
    if message_id not in user_answers[chat_id]:
        user_answers[chat_id][message_id] = {}
    user_answers[chat_id][message_id][user_id] = selected

    # Keyingi savol
    test["index"] += 1
    await send_question(chat_id, context)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("unit", unit_command))
    app.add_handler(CallbackQueryHandler(button))

    print("Bot ishga tushdi...")
    
    # Railway webhook sozlash
    if WEBHOOK_URL:
        print(f"Webhook URL: {WEBHOOK_URL}")
        app.run_webhook(
            listen="0.0.0.0",
            port=PORT,
            url_path=BOT_TOKEN,
            webhook_url=f"{WEBHOOK_URL}/{BOT_TOKEN}"
        )
    else:
        print("Webhook URL topilmadi, polling ishlatilmoqda...")
        app.run_polling()

if __name__ == "__main__":
    main()
}

# ======================= LOGGING =======================
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

active_tests = {}
user_answers = {}

def generate_question(unit_data):
    word, meaning = random.choice(list(unit_data.items()))
    correct = meaning
    wrong_options = [v for k, v in unit_data.items() if v != correct]
    wrongs = random.sample(wrong_options, min(3, len(wrong_options)))
    options = wrongs + [correct]
    random.shuffle(options)
    return word, correct, options

def get_keyboard(options):
    keyboard = [[InlineKeyboardButton(opt, callback_data=opt)] for opt in options]
    return InlineKeyboardMarkup(keyboard)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "😁 Salom! Men Vocabulary Bot man.\n"
        "Menda 30 ta unit bor!\n"
        "Meni guruhga qo'shing va admin qiling — shunda testlar ishlaydi 🚀"
    )

async def unit_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id

    if user_id not in ADMIN_IDS:
        await update.message.reply_text("❌ Faqat admin test boshlashi mumkin!")
        return

    if not context.args:
        await update.message.reply_text("Unit raqamini kiriting. Misol: /unit 7")
        return

    unit_num = context.args[0]
    if unit_num not in vocab:
        await update.message.reply_text(f"Unit {unit_num} mavjud emas! Faqat 1-30 unitlar mavjud.")
        return

    unit_data = vocab[unit_num]
    questions = []
    for _ in range(20):
        word, correct, options = generate_question(unit_data)
        questions.append({"word": word, "correct": correct, "options": options})

    active_tests[chat_id] = {
        "unit": unit_num,
        "questions": questions,
        "index": 0,
        "scores": {}
    }
    
    user_answers[chat_id] = {}

    await update.message.reply_text(
        f"🎲 'Unit {unit_num}' testiga tayyorlaning!\n"
        "🖊 20 ta savol\n\n"
        "Test boshlandi!"
    )
    
    await send_question(chat_id, context)

async def send_question(chat_id, context: ContextTypes.DEFAULT_TYPE):
    test = active_tests.get(chat_id)
    if not test:
        return
        
    idx = test["index"]
    if idx >= len(test["questions"]):
        # Test yakunlandi
        scores = test["scores"]
        leaderboard = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        msg = f"🏁 Unit {test['unit']} testi yakunlandi!\n20 ta savol berildi.\n\n"
        medals = ["🥇", "🥈", "🥉"]
        
        for i, (user_id, score) in enumerate(leaderboard[:3]):
            try:
                user = await context.bot.get_chat(user_id)
                user_name = user.first_name or f"User {user_id}"
            except:
                user_name = f"User {user_id}"
            msg += f"{medals[i] if i < 3 else '   '} {user_name} – {score}/20\n"
        
        if not leaderboard:
            msg += "Hech kim javob bermadi 😔"
        
        await context.bot.send_message(chat_id, msg)
        active_tests.pop(chat_id, None)
        user_answers.pop(chat_id, None)
        return

    question = test["questions"][idx]
    keyboard = get_keyboard(question["options"])
    message = await context.bot.send_message(
        chat_id, 
        f"❓ {question['word']} so'zining ma'nosini toping:\n\nSavol {idx + 1}/20", 
        reply_markup=keyboard
    )
    
    user_answers[chat_id][message.message_id] = {}

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id
    chat_id = query.message.chat.id
    message_id = query.message.message_id
    
    await query.answer()
    
    test = active_tests.get(chat_id)
    if not test:
        await query.edit_message_text("Test tugadi.")
        return

    idx = test["index"]
    question = test["questions"][idx]

    # User allaqachon javob berganmi tekshirish
    if user_answers.get(chat_id, {}).get(message_id, {}).get(user_id):
        await query.answer("Siz allaqachon javob berdingiz!", show_alert=True)
        return

    selected = query.data
    correct = question["correct"]

    # Score update
    if user_id not in test["scores"]:
        test["scores"][user_id] = 0
        
    if selected == correct:
        test["scores"][user_id] += 1
        await query.answer("✅ To'g'ri!")
    else:
        await query.answer("❌ Noto'g'ri!")

    # User javobini saqlash
    if chat_id not in user_answers:
        user_answers[chat_id] = {}
    if message_id not in user_answers[chat_id]:
        user_answers[chat_id][message_id] = {}
    user_answers[chat_id][message_id][user_id] = selected

    # Keyingi savol
    test["index"] += 1
    await send_question(chat_id, context)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("unit", unit_command))
    app.add_handler(CallbackQueryHandler(button))

    print("Bot ishga tushdi...")
    
    # Railway webhook sozlash
    if WEBHOOK_URL:
        print(f"Webhook URL: {WEBHOOK_URL}")
        app.run_webhook(
            listen="0.0.0.0",
            port=PORT,
            url_path=BOT_TOKEN,
            webhook_url=f"{WEBHOOK_URL}/{BOT_TOKEN}"
        )
    else:
        print("Webhook URL topilmadi, polling ishlatilmoqda...")
        app.run_polling()

if __name__ == "__main__":
    main()
