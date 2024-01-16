# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "14356452"))
    API_HASH = getenv("API_HASH", "cac21249a0c6373a1b742afb8dbc9cb7")
    BOT_TOKEN = getenv("BOT_TOKEN", "6704921667:AAGKp6AJSmEcGUKiX4Jhg_2xlPO3YBHqGMc")
    FSUB = getenv("FSUB", "Kc_Films_2024")
    CHID = int(getenv("CHID", "-1001825196084"))
    SUDO = list(map(int, getenv("SUDO", "5720092781").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://Nandesha:alabal18@cluster0.6qjsxnq.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
