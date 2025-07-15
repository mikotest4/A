from os import environ, getenv
import re
import os

id_pattern = re.compile(r"^.\d+$")


def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


ADMIN = int(getenv("ADMIN", "7970350353"))
YAE_MIKO_PIC = os.environ.get("SILICON_PIC", "https://graph.org/file/f2a14c12b3858c49766aa-92d3f438ab56f6df1d.jpg")
API_ID = int(getenv("API_ID", "27704224"))
API_HASH = str(getenv("API_HASH", "c2e33826d757fe113bc154fcfabc987d"))
BOT_TOKEN = str(getenv("BOT_TOKEN", "7282397670:AAFT8xuILQhSFe0bYofsDQEr4cDNFY2Y_tE"))
FORCE_SUB = os.environ.get("FORCE_SUB", "") 
MONGO_DB = str(getenv("MONGO_DB", "mongodb+srv://Koi:aloksingh@cluster0.86wo9.mongodb.net/?retryWrites=true&w=majority",))
DEF_CAP = str(getenv("DEF_CAP","",))
