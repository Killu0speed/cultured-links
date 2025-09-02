import os
from os import environ
import logging
from logging.handlers import RotatingFileHandler

#Recommended
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "8458865116:AAEGvy3EwrycmlAX8yF7hIoR8mvbr8ojJfc")
APP_ID = int(os.environ.get("APP_ID", "27108998"))
API_HASH = os.environ.get("API_HASH", "f4fc03493766db361d7e85ed8974fe2f")

##---------------------------------------------------------------------------------------------------

#Main 
OWNER_ID = int(os.environ.get("OWNER_ID", "5191566338"))
PORT = os.environ.get("PORT", "8013")

##---------------------------------------------------------------------------------------------------

#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://narutokilluaa_db_user:NhFdVndD2aX3EEaQ@cluster0.i9thmyb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

##---------------------------------------------------------------------------------------------------

#Default
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5191566338").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

##---------------------------------------------------------------------------------------------------        

#Default
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = None

##---------------------------------------------------------------------------------------------------

#Admin == OWNERID
ADMINS.append(OWNER_ID)
ADMINS.append(5191566338)

##---------------------------------------------------------------------------------------------------

#Default
LOG_FILE_NAME = "links-sharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
##---------------------------------------------------------------------------------------------------
