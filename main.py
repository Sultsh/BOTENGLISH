# Telegram Vocabulary Test Bot (4000 Essential English Words)
# Fully working structure – questions, timers, scoring, admin-only start
# NOTE: Fill vocab data for Units 1–30 inside the vocab dictionary.

import asyncio
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import (Application, CommandHandler, CallbackQueryHandler,
                          ContextTypes)

BOT_TOKEN = "8538557025:AAHxyGoWwPnjnMIXzwngx8_CZQMBz9yM0Eg"

# ==========================
#  VOCABULARY DATABASE (1–30)
# ==========================
# Faqat misol uchun Unit 1 qo'yilgan — qolganlarni to'ldirasiz.
vocab = {
    "1": {
        "afraid": "qo'rqmoq",
        "agree": "rozi bo'lmoq", 
        "angry": "jahldor",
        "arrive": "yetib kelmoq",
        "attack": "hujum qilmoq",
        "bottom": "tagi osti",
        "clever": "aqilli",
        "cruel": "shafqatsiz",
        "finally": "nihoyat",
        "hide": "yashirmoq",
        "hunt": "ovlamoq",
        "lot": "ko'p", 
        "middle": "o'rta",
        "moment": "lahza",
        "pleased": "mamnun",
        "promise": "va'da bermoq",
        "reply": "javob bermoq",
        "safe": "xavfsiz",
        "trick": "hiyla",
        "well": "yaxshi"
    },
    "2": {
        "allow": "ruxsat bermoq",
        "announce": "e'lon qilmoq",
        "beside": "yonida",
        "challenge": "murojaat",
        "claim": "da'vo qilmoq",
        "condition": "shart",
        "contribute": "hissa qo'shmoq",
        "difference": "farq",
        "divide": "bo'lmoq",
        "expert": "mutaxassis",
        "famous": "mashhur",
        "force": "kuch",
        "harm": "zarar",
        "lay": "yotqizmoq",
        "peace": "tinchlik",
        "prince": "shahzoda",
        "protect": "himoya qilmoq",
        "sense": "his",
        "sudden": "toshgan",
        "therefore": "shuning uchun"
    },
    "3": {
        "accept": "qabul qilmoq",
        "arrange": "tartibga solmoq",
        "attend": "qatnashmoq",
        "balance": "muvozanat",
        "compare": "solishtirmoq",
        "consider": "o'ylamoq",
        "disease": "kasallik",
        "essential": "zarur",
        "event": "hodisa",
        "familiar": "tanish",
        "future": "kelajak",
        "include": "o'z ichiga olmoq",
        "manage": "boshqarmoq",
        "necessary": "zarur",
        "organize": "tashkil qilmoq",
        "public": "ommaviy",
        "purpose": "maqsad",
        "respect": "hurmat",
        "separate": "alohida",
        "several": "bir nechta"
    },
    "4": {
        "achieve": "erishmoq",
        "advice": "maslahat",
        "already": "allaqachon",
        "basic": "asosiy",
        "blood": "qon",
        "carry": "ko'tarmoq",
        "connect": "ulamoq",
        "continue": "davom etmoq",
        "decision": "qaror",
        "deliver": "yetkazmoq",
        "describe": "tasvirlamoq",
        "education": "ta'lim",
        "effort": "harakat",
        "enemy": "dushman",
        "except": "dan tashqari",
        "increase": "oshirmoq",
        "indicate": "ko'rsatmoq",
        "instead": "o'rniga",
        "intend": "niyat qilmoq",
        "issue": "masala"
    },
    "5": {
        "actual": "haqiqiy",
        "appropriate": "munosib",
        "available": "mavjud",
        "behavior": "xulq-atvor",
        "benefit": "foyda",
        "certain": "aniq",
        "community": "jamiyat",
        "concern": "tashvish",
        "consistent": "izchil",
        "create": "yaratmoq",
        "culture": "madaniyat",
        "current": "joriy",
        "development": "rivojlanish",
        "economic": "iqtisodiy",
        "environment": "muhit",
        "establish": "barpo qilmoq",
        "evidence": "dalil",
        "factor": "omil",
        "financial": "moliyaviy",
        "function": "funktsiya"
    },
    "6": {
        "ability": "qobiliyat",
        "access": "kirish",
        "account": "hisob",
        "achieve": "erishmoq",
        "acquire": "egallamoq",
        "action": "harakat",
        "activity": "faoliyat",
        "adult": "katta yoshli",
        "affect": "ta'sir qilmoq",
        "after": "keyin",
        "again": "yana",
        "against": "qarshi",
        "age": "yosh",
        "agency": "agentlik",
        "agent": "agent",
        "ago": "oldin",
        "agree": "rozi bo'lmoq",
        "agreement": "kelishuv",
        "ahead": "oldinda",
        "air": "havo"
    },
    "7": {
        "analysis": "tahlil",
        "apply": "qo'llamoq",
        "approach": "yondashuv",
        "area": "maydon",
        "assess": "baholamoq",
        "assume": "faraz qilmoq",
        "authority": "huquq",
        "available": "mavjud",
        "benefit": "foyda",
        "concept": "tushuncha",
        "conduct": "o'tkazmoq",
        "consist": "tashkil etmoq",
        "constitute": "tashkil qilmoq",
        "context": "kontekst",
        "contract": "shartnoma",
        "create": "yaratmoq",
        "data": "ma'lumot",
        "define": "aniqlamoq",
        "derive": "kelib chiqmoq",
        "distribute": "taqsimlamoq"
    },
    "8": {
        "economy": "iqtisodiyot",
        "environment": "atrof-muhit",
        "establish": "o'rnatmoq",
        "estimate": "baholamoq",
        "evident": "aniq",
        "export": "eksport",
        "factor": "omil",
        "finance": "moliyalashtirmoq",
        "formula": "formula",
        "function": "vazifa",
        "identify": "aniqlamoq",
        "income": "daromad",
        "indicate": "ko'rsatmoq",
        "individual": "individual",
        "interpret": "izohlamoq",
        "involve": "jalb qilmoq",
        "issue": "nashr",
        "labour": "mehnat",
        "legal": "qonuniy",
        "legislate": "qonun chiqarmoq"
    },
    "9": {
        "major": "asosiy",
        "method": "usul",
        "occur": "yuz bermoq",
        "percent": "foiz",
        "period": "davr",
        "policy": "siyosat",
        "principle": "tamoyil",
        "proceed": "davom etmoq",
        "process": "jarayon",
        "require": "talab qilmoq",
        "research": "tadqiqot",
        "respond": "javob bermoq",
        "role": "rol",
        "section": "bo'lim",
        "sector": "soha",
        "significant": "muhim",
        "similar": "o'xshash",
        "source": "manba",
        "specific": "maxsus",
        "structure": "tuzilma"
    },
    "10": {
        "theory": "nazariya",
        "vary": "farq qilmoq",
        "achieve": "erishmoq",
        "acquisition": "sotib olish",
        "administration": "ma'muriyat",
        "affect": "ta'sir",
        "appropriate": "munosib",
        "aspect": "jihat",
        "assist": "yordam",
        "category": "toifa",
        "chapter": "bob",
        "commission": "komissiya",
        "community": "jamoa",
        "complex": "murakkab",
        "compute": "hisoblamoq",
        "conclude": "xulosa qilmoq",
        "conduct": "o'tkazish",
        "consequent": "natijada",
        "construct": "qurmoq",
        "consume": "iste'mol qilmoq"
    },
        "11": {
        "credit": "kredit",
        "culture": "madaniyat",
        "design": "dizayn",
        "distinct": "alohida",
        "element": "element",
        "equate": "tenglashtirmoq",
        "evaluate": "baholamoq",
        "feature": "xususiyat",
        "final": "yakuniy",
        "focus": "diqqat",
        "impact": "ta'sir",
        "injury": "jarohat",
        "institute": "institut",
        "invest": "sarmoya kiritmoq",
        "item": "element",
        "journal": "jurnal",
        "maintain": "saqlamoq",
        "normal": "oddiy",
        "obtain": "olmoq",
        "participate": "qatnashmoq"
    },
    "12": {
        "perceive": "sezmoq",
        "positive": "ijobiy",
        "potential": "potentsial",
        "previous": "oldingi",
        "primary": "birlamchi",
        "purchase": "sotib olish",
        "range": "diapazon",
        "region": "mintaqa",
        "register": "ro'yxatdan o'tmoq",
        "regulate": "tartibga solmoq",
        "relevant": "muvofiq",
        "resource": "resurs",
        "restrict": "cheklamoq",
        "secure": "xavfsiz",
        "seek": "izlamoq",
        "select": "tanlamoq",
        "site": "sayt",
        "strategy": "strategiya",
        "survey": "so'rovnoma",
        "text": "matn"
    },
    "13": {
        "tradition": "an'ana",
        "transfer": "o'tkazmoq",
        "alternative": "alternativ",
        "circumstance": "holat",
        "comment": "sharh",
        "compensate": "kompensatsiya qilmoq",
        "component": "komponent",
        "consent": "rozilik",
        "considerable": "sezilarli",
        "constant": "doimiy",
        "constrain": "cheklamoq",
        "contribute": "hissa qo'shmoq",
        "convene": "chaqirmoq",
        "coordinate": "muvofiqlashtirmoq",
        "core": "yadro",
        "corporate": "korporativ",
        "correspond": "mos kelmoq",
        "criteria": "mezonlar",
        "dedicate": "bag'ishlamoq",
        "demonstrate": "namoyish etmoq"
    },
    "14": {
        "document": "hujjat",
        "domain": "domen",
        "emphasis": "urg'u",
        "ensure": "ta'minlamoq",
        "exclude": "chiqarib tashlamoq",
        "framework": "ramka",
        "fund": "fond",
        "illustrate": "tasvirlamoq",
        "immigrate": "ko'chib kelmoq",
        "imply": "anglatmoq",
        "initial": "dastlabki",
        "instance": "misol",
        "interact": "o'zaro ta'sir",
        "justify": "asoslamoq",
        "layer": "qatlam",
        "link": "havola",
        "locate": "joylashtirmoq",
        "maximize": "maksimallashtirmoq",
        "minor": "kichik",
        "negate": "inkor etmoq"
    },
    "15": {
        "outcome": "natija",
        "partner": "hamkor",
        "philosophy": "falsafa",
        "physical": "jismoniy",
        "proportion": "nisbat",
        "publish": "nashr etmoq",
        "react": "reaksiya",
        "remove": "olib tashlamoq",
        "scheme": "reja",
        "sequence": "ketma-ketlik",
        "sex": "jins",
        "shift": "o'zgartirmoq",
        "specify": "aniqlamoq",
        "sufficient": "yetarli",
        "task": "vazifa",
        "technical": "texnik",
        "technique": "usul",
        "technology": "texnologiya",
        "valid": "amal qiluvchi",
        "volume": "hajm"
    },
    "16": {
        "abandon": "tark etmoq",
        "accompany": "hamrohlik qilmoq",
        "accumulate": "to'plamoq",
        "ambiguous": "noaniq",
        "amend": "o'zgartirmoq",
        "apparent": "aydin",
        "appreciate": "qadrlamoq",
        "arbitrary": "o'zboshimchalik",
        "ascertain": "aniqlamoq",
        "assume": "faraz qilmoq",
        "attain": "erishmoq",
        "attribute": "xususiyat",
        "augment": "kuchaytirmoq",
        "benign": "yaxshi",
        "brevity": "qisqalik",
        "capable": "qodir",
        "cease": "to'xtatmoq",
        "coherent": "mantiqiy",
        "coincide": "to'g'ri kelmoq",
        "commence": "boshlanmoq"
    },
    "17": {
        "compatible": "mos",
        "compel": "majbur qilmoq",
        "conceive": "tushunmoq",
        "concurrent": "bir vaqtda",
        "confine": "cheklamoq",
        "conform": "mos kelmoq",
        "consecutive": "ketma-ket",
        "considerable": "katta",
        "consistent": "izchil",
        "conspicuous": "ko'zga tashlanadigan",
        "contemporary": "zamonaviy",
        "contradict": "zid kelmoq",
        "crucial": "muhim",
        "cumulative": "to'plangan",
        "defer": "kechiktirmoq",
        "definite": "aniq",
        "demonstrate": "ko'rsatmoq",
        "denote": "bildirmoq",
        "depict": "tasvirlamoq",
        "derive": "kelib chiqmoq"
    },
    "18": {
        "designate": "belgilamoq",
        "deviate": "chekinmoq",
        "differentiate": "farqlamoq",
        "diminish": "kamaytirmoq",
        "discrete": "alohida",
        "displace": "siljitmoq",
        "disseminate": "tarqatmoq",
        "diverse": "xilma-xil",
        "dominant": "ustun",
        "elaborate": "batafsil",
        "elicit": "olmoq",
        "emerge": "paydo bo'lmoq",
        "enhance": "yaxshilamoq",
        "enormous": "ulkan",
        "encompass": "o'z ichiga olmoq",
        "endure": "bardosh bermoq",
        "enhance": "oshirmoq",
        "entity": "ob'ekt",
        "equivalent": "teng",
        "erratic": "beqaror"
    },
    "19": {
        "establish": "o'rnatmoq",
        "evaluate": "baholamoq",
        "evident": "aniq",
        "exclude": "chiqarib tashlamoq",
        "explicit": "ochiq",
        "facilitate": "osonlashtirmoq",
        "fundamental": "asosiy",
        "generate": "yaratmoq",
        "hypothesis": "gipoteza",
        "implement": "amalga oshirmoq",
        "imply": "anglatmoq",
        "infer": "xulosa qilmoq",
        "inherent": "tabiiy",
        "inhibit": "to'sqinlik qilmoq",
        "integrate": "birlashtirmoq",
        "intervene": "aralashmoq",
        "intrinsic": "ichki",
        "invariably": "doim",
        "investigate": "tadqiq qilmoq",
        "invoke": "chaqirmoq"
    },
    "20": {
        "isolate": "ajratmoq",
        "mediate": "vositachilik qilmoq",
        "migrate": "ko'chib o'tmoq",
        "minimal": "minimal",
        "monitor": "kuzatmoq",
        "mutual": "o'zaro",
        "negate": "inkor etmoq",
        "neutral": "neytral",
        "notion": "tushuncha",
        "notwithstanding": "ga qaramasdan",
        "obtain": "olmoq",
        "obvious": "aydin",
        "occur": "yuz bermoq",
        "paradigm": "paradigma",
        "phenomenon": "hodisa",
        "portion": "qism",
        "precede": "oldin kelmoq",
        "precise": "aniq",
        "presume": "faraz qilmoq",
        "prime": "asosiy"
    },
    "21": {
        "priority": "ustuvorlik",
        "proceed": "davom etmoq",
        "profound": "chuqur",
        "prohibit": "taqiqlamoq",
        "prominent": "taniqli",
        "proportion": "nisbat",
        "provoke": "qo'zg'atmoq",
        "radical": "radikal",
        "random": "tasodifiy",
        "reinforce": "mustahkamlamoq",
        "reject": "rad etmoq",
        "reluctant": "istaksiz",
        "require": "talab qilmoq",
        "resolve": "hal qilmoq",
        "restrict": "cheklamoq",
        "retain": "saqlamoq",
        "reveal": "ochib bermoq",
        "scope": "doira",
        "sequence": "ketma-ketlik",
        "severe": "qattiq"
    },
    "22": {
        "shift": "o'zgarish",
        "significant": "muhim",
        "similar": "o'xshash",
        "simulate": "simulyatsiya qilmoq",
        "simultaneous": "bir vaqtda",
        "sophisticated": "murakkab",
        "specify": "aniqlamoq",
        "spontaneous": "o'ziga xos",
        "stable": "barqaror",
        "statistic": "statistika",
        "status": "maqom",
        "subsequent": "keyingi",
        "substantial": "sezilarli",
        "subtle": "nozik",
        "sufficient": "yetarli",
        "summary": "xulosa",
        "supplement": "qo'shimcha",
        "suspend": "to'xtatmoq",
        "sustain": "qo'llab-quvvatlamoq",
        "symbol": "belgi"
    },
    "23": {
        "taught": "o'rgatilgan",
        "temporary": "vaqtincha",
        "terminate": "tugatmoq",
        "theme": "mavzu",
        "thereby": "shu orqali",
        "uniform": "bir xil",
        "unique": "noyob",
        "utilize": "foydalanmoq",
        "valid": "amal qiluvchi",
        "vary": "farq qilmoq",
        "verbal": "og'zaki",
        "verify": "tekshirmoq",
        "via": "orqali",
        "violate": "buzmoq",
        "virtual": "virtual",
        "visible": "ko'rinadigan",
        "visual": "vizual",
        "volume": "hajm",
        "voluntary": "ixtiyoriy",
        "welfare": "farovonlik"
    },
    "24": {
        "whereas": "holbuki",
        "whereby": "qaysiki",
        "widespread": "keng tarqalgan",
        "abstract": "mavhum",
        "accurate": "aniq",
        "acknowledge": "tan olmoq",
        "aggregate": "yig'indi",
        "allocate": "ajratmoq",
        "assign": "tayinlamoq",
        "attach": "biriktirmoq",
        "author": "muallif",
        "bond": "bog'lash",
        "brief": "qisqa",
        "capable": "qodir",
        "cite": "iqtibos keltirmoq",
        "cooperate": "hamkorlik qilmoq",
        "discriminate": "ajratmoq",
        "display": "namoyish",
        "diverse": "xilma-xil",
        "domain": "soha"
    },
    "25": {
        "edit": "tahrir qilmoq",
        "enhance": "yaxshilamoq",
        "estate": "mulk",
        "exceed": "oshirmoq",
        "expert": "mutaxassis",
        "explicit": "ochiq",
        "federal": "federal",
        "fee": "haq",
        "flexible": "moslashuvchan",
        "furthermore": "bundan tashqari",
        "gender": "jins",
        "ignorant": "bilimsiz",
        "incentive": "rag'bat",
        "incidence": "holat",
        "incorporate": "o'z ichiga olmoq",
        "index": "indeks",
        "inhibit": "to'sqinlik qilmoq",
        "initiate": "boshlash",
        "input": "kirish",
        "instruct": "ko'rsatma bermoq"
    },
    "26": {
        "intelligence": "aql",
        "interval": "interval",
        "lecture": "ma'ruza",
        "migration": "migratsiya",
        "minimum": "minimum",
        "ministry": "vazirlik",
        "motivate": "rag'batlantirmoq",
        "nevertheless": "shunga qaramay",
        "overseas": "chet el",
        "preceding": "oldingi",
        "presumption": "faraz",
        "rational": "maqbul",
        "recovery": "tiklanish",
        "reveal": "oshkor qilmoq",
        "scope": "doira",
        "subsidy": "subsidiya",
        "trace": "iz",
        "transform": "o'zgartirmoq",
        "transport": "transport",
        "underlying": "asosiy"
    },
    "27": {
        "utility": "foydalilik",
        "adapt": "moslashmoq",
        "adequate": "yetarli",
        "adjacent": "qo'shni",
        "adjust": "sozlamoq",
        "administrate": "boshqarmoq",
        "adult": "katta yoshli",
        "advocate": "tarafdor",
        "aid": "yordam",
        "channel": "kanal",
        "chemical": "kimyoviy",
        "clause": "band",
        "compete": "raqobatlashmoq",
        "comprise": "o'z ichiga olmoq",
        "compute": "hisoblamoq",
        "conclude": "xulosa qilmoq",
        "concurrent": "bir vaqtda",
        "confirm": "tasdiqlamoq",
        "conflict": "ziddiyat",
        "contact": "aloqa"
    },
    "28": {
        "decline": "pasayish",
        "discrete": "alohida",
        "draft": "qoralama",
        "enable": "imkon bermoq",
        "energy": "energiya",
        "enforce": "amalga oshirmoq",
        "entity": "ob'ekt",
        "equivalent": "teng",
        "evolve": "rivojlanmoq",
        "expand": "kengaytirmoq",
        "expose": "oshkor qilmoq",
        "external": "tashqi",
        "facilitate": "osonlashtirmoq",
        "fundamental": "asosiy",
        "generate": "yaratmoq",
        "generation": "avlod",
        "image": "tasvir",
        "liberal": "liberal",
        "license": "litsenziya",
        "logic": "mantiq"
    },
    "29": {
        "margin": "chegara",
        "medical": "tibbiy",
        "mental": "aqliy",
        "modify": "o'zgartirmoq",
        "monitor": "kuzatuvchi",
        "network": "tarmoq",
        "notion": "tushuncha",
        "objective": "maqsad",
        "orient": "yo'naltirmoq",
        "perspective": "nuqtai nazar",
        "precise": "aniq",
        "prime": "asosiy",
        "psychology": "psixologiya",
        "pursue": "ergashmoq",
        "ratio": "nisbat",
        "reject": "rad etmoq",
        "revenue": "daromad",
        "stable": "barqaror",
        "style": "uslub",
        "substitute": "o'rinbosar"
    },
    "30": {
        "supervise": "nazorat qilmoq",
        "supplement": "qo'shimcha",
        "survive": "omon qolmoq",
        "sustain": "qo'llab-quvvatlamoq",
        "symbol": "ramz",
        "target": "maqsad",
        "tradition": "an'ana",
        "transfer": "o'tkazish",
        "trend": "trend",
        "ultimate": "yakuniy",
        "unique": "noyob",
        "visible": "ko'rinadigan",
        "voluntary": "ixtiyoriy",
        "welfare": "farovonlik",
        "whereas": "holbuki",
        "whereby": "qaysiki",
        "widespread": "keng tarqalgan",
        "accommodate": "joylashtirmoq",
        "analogy": "o'xshashlik",
        "anticipate": "kutmoq"
    }
    # 2–30 units shu joyga qo'shiladi
}

# TEST SESSION STRUCTURE
sessions = {}  # {chat_id: {...}}

# ===============
# START COMMAND
# ===============
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    txt = (
        "😁 Salom! Men @SULTSH_YT tomonidan yaratilgan Lug‘at Bot man.\n"
        "Menda 30 ta unit (bo‘lim) bor!\n"
        "Meni guruhga qo‘shing va admin qiling — shunda testlar ishlaydi 🚀"
    )
    await update.message.reply_text(txt)

# ===============
# CHECK ADMIN
# ===============
async def is_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id
    admins = await context.bot.get_chat_administrators(chat_id)
    admin_list = [adm.user.id for adm in admins]
    return user_id in admin_list

# ==================
# /unitX TEST STARTER
# ==================
async def unit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.type == "private":
        return await update.message.reply_text("❗ Test faqat guruhlarda ishlaydi.")

    if not await is_admin(update, context):
        return await update.message.reply_text("⛔ Faqat admin test boshlashi mumkin.")

    # Extract unit number
    cmd = update.message.text.replace("/unit", "").strip()
    if cmd not in vocab:
        return await update.message.reply_text("❗ Bunday unit yo'q.")

    chat_id = update.effective_chat.id

    # PREVIEW SCREEN
    keyboard = [[InlineKeyboardButton("🚀 Boshlash", callback_data=f"starttest_{cmd}")]]
    await update.message.reply_text(
        f"🎲 \"4000 Essential English Words — Unit {cmd}\" testiga tayyorlaning!\n"
        "🖊 20 ta savol\n"
        "⏱ Har bir savol uchun 10 soniya",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# =============================
# “Start Test” BUTTON HANDLER
# =============================
async def start_test(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    chat_id = update.effective_chat.id
    unit_number = query.data.split("_")[1]

    words = list(vocab[unit_number].items())
    words = words[:20]  # 20-ta so'z
    sessions[chat_id] = {
        "unit": unit_number,
        "index": 0,
        "words": words,
        "scores": {}  # {user_id: ball}
    }

    await query.edit_message_text("Test boshlandi!")
    await send_question(chat_id, context)

# ======================
# SEND QUESTION FUNCTION
# ======================
async def send_question(chat_id, context):
    session = sessions.get(chat_id)
    if not session:
        return

    idx = session["index"]
    if idx >= 20:
        return await finish_test(chat_id, context)

    eng, uz = session["words"][idx]

    # Build answer choices
    wrong = []
    for u in vocab[session["unit"]].values():
        if u != uz:
            wrong.append(u)
        if len(wrong) == 3:
            break

  import random
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

# ======================
# SEND QUESTION FUNCTION
# ======================
async def send_question(chat_id, context):
    session = sessions.get(chat_id)
    if not session:
        return

    idx = session["index"]
    if idx >= 20:
        return await finish_test(chat_id, context)

    eng, uz = session["words"][idx]

    # Build answer choices
    wrong = [u for u in vocab[session["unit"]].values() if u != uz]
    wrong_choices = random.sample(wrong, 3)  # 3 noto'g'ri javob
    opts = wrong_choices + [uz]
    random.shuffle(opts)

    # Inline keyboard – har bir variant alohida qatorda
    keyboard = [[InlineKeyboardButton(opt, callback_data=f"ans_{idx}_{opt}")] for opt in opts]

    # Ask
    await context.bot.send_message(
        chat_id,
        f"❓ <b>{eng}</b> so‘zining ma’nosini toping:",
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

    # Auto move next after 10 seconds
    await asyncio.sleep(10)
    if session["index"] == idx:
        session["index"] += 1
        await send_question(chat_id, context)

# ======================
# ANSWER HANDLER
# ======================
async def answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    chat_id = update.effective_chat.id
    user_id = update.effective_user.id

    session = sessions.get(chat_id)
    if not session:
        return

    _, q_index, chosen = query.data.split("_", 2)
    q_index = int(q_index)

    # User already answered? block.
    if user_id in session.get(f"answered_{q_index}", []):
        return await query.edit_message_text("⛔ Siz allaqachon javob bergansiz.")

    correct = session["words"][q_index][1]

    # Save answer
    session.setdefault(f"answered_{q_index}", []).append(user_id)

    if chosen == correct:
        session["scores"][user_id] = session["scores"].get(user_id, 0) + 1
        txt = "✅ To‘g‘ri!"
    else:
        txt = "❌ Noto‘g‘ri!"

    await query.edit_message_text(txt)

# ==================
# FINISH TEST
# ==================
async def finish_test(chat_id, context):
    session = sessions.get(chat_id)
    if not session:
        return

    unit = session["unit"]
    scores = session["scores"]

    sorted_score = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    result = f"🏁 Unit {unit} testi yakunlandi!\n20 ta savol berildi.\n\n"

    medal = ["🥇", "🥈", "🥉"]
    for i, (uid, sc) in enumerate(sorted_score[:3]):
        user = await context.bot.get_chat_member(chat_id, uid)
        name = user.user.first_name
        result += f"{medal[i]} {name} – {sc}\n"

    await context.bot.send_message(chat_id, result)
    del sessions[chat_id]

# ==============
# MAIN
# ==============
def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("unit", unit))
    app.add_handler(CommandHandler([f"unit{i}" for i in range(1,30)], unit))
    app.add_handler(CallbackQueryHandler(start_test, pattern=r"starttest_"))
    app.add_handler(CallbackQueryHandler(answer, pattern=r"ans_"))

    app.run_polling()


if __name__ == "__main__":
    main()


