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
SILICON_PIC = os.environ.get("SILICON_PIC", "https://telegra.ph/file/21a8e96b45cd6ac4d3da6.jpg")
API_ID = int(getenv("API_ID", "27704224"))
API_HASH = str(getenv("API_HASH", "c2e33826d757fe113bc154fcfabc987d"))
BOT_TOKEN = str(getenv("BOT_TOKEN", "7819249411:AAGTXBgQ7l4Daz-wJG1lkx4Ubf1bB1e3sNI"))
FORCE_SUB = os.environ.get("FORCE_SUB", "") 
MONGO_DB = str(getenv("MONGO_DB", "mongodb+srv://Koi:aloksingh@cluster0.86wo9.mongodb.net/?retryWrites=true&w=majority",))
DEF_CAP = str(getenv("DEF_CAP","",))
