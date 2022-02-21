
import os
import time
import logging
from logging.handlers import RotatingFileHandler

class Config(object):

# Get a bot token from botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

# Get from my.telegram.org (or @UseTGXBot)
APP_ID = int(os.environ.get("APP_ID", ""))

# Get from my.telegram.org (or @UseTGXBot)
API_HASH = os.environ.get("API_HASH", "")


# Database URL from https://cloud.mongodb.com/
DATABASE_URI = os.environ.get("DATABASE_URI", "")

# Your database name from mongoDB
 DATABASE_NAME = str(os.environ.get("DATABASE_NAME", "Cluster0"))

# ID of users that can use the bot commands
AUTH_USERS = set(str(x) for x in os.environ.get("AUTH_USERS", "").split())

# To save user details (Usefull for getting userinfo and total user counts)
# May reduce filter capacity :(
# Give yes or no
SAVE_USER = os.environ.get("SAVE_USER", "no").lower()

# Go to https://dashboard.heroku.com/account, scroll down and press Reveal API
# To check dyno status
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "")

# Generate a user session string 
TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "")

# ID of Channel from which the bot shoul search files
MAINCHANNEL_ID = os.environ.get("MAINCHANNEL_ID", "")

# OPTIONAL - To set alternate BOT COMMANDS
ADD_FILTER_CMD = os.environ.get("ADD_FILTER_CMD", "add")
DELETE_FILTER_CMD = os.environ.get("DELETE_FILTER_CMDD", "del")
DELETE_ALL_CMD = os.environ.get("DELETE_ALL_CMDD", "delall")
CONNECT_COMMAND = os.environ.get("CONNECT_COMMANDD", "connect")
DISCONNECT_COMMAND = os.environ.get("DISCONNECT_COMMANDD", "disconnect")


# To record start time of bot
BOT_START_TIME = time.time()



TG_BOT_SESSION = os.environ.get("TG_BOT_SESSION", "bot")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
LOG_FILE_NAME = "filterbot.txt"

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
