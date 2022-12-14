import os
import logging 
from pyrogram import Client
from pyromod import listen
from config import Config

# enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

LOG = logging.getLogger(__name__)


ENV = bool(os.environ.get("ENV",False))

if ENV:
    API_ID=int(os.environ.get("API_ID",None))
    API_HASH=str(os.environ.get("API_HASH",None))
    TOKEN=str(os.environ.get("TOKEN",None))
    NETWORK_IMG=str(os.environ.get("NETWORK_IMG",None))
    NETWORK_NAME=str(os.environ.get("NETWORK_NAME",None))
    NETWORK_USERNAME=str(os.environ.get("NETWORK_USERNAME",None))
    TOS_LINK=str(os.environ.get("TOS_LINK", None)) # terms and conditions of your network if not have any then just leave it
    VERIFICATION_CHANNEL_ID=int(os.environ.get("VERIFICATION_CHANNEL_ID",None))
    VERIFICATION_CHANNEL_USERNAME=str(os.environ.get("VERIFICATION_CHANNEL_USERNAME",None))
    ADMINS = list(int(i) for i in os.environ.get("ADMINS", " ").split(" "))
    HQ_ID=int(os.environ.get("HQ_ID",None))
    HQ_USERNAME=str(os.environ.get("HQ_USERNAME",None))

  
else:
    API_ID=Config.API_ID
    API_HASH=Config.API_HASH
    TOKEN=Config.TOKEN
    TOS_LINK=Config.TOS_LINK
    NETWORK_NAME = Config.NETWORK_NAME
    HQ_USERNAME = Config.HQ_USERNAME
    NETWORK_USERNAME=Config.NETWORK_USERNAME
    VERIFICATION_CHANNEL_USERNAME = Config.VERIFICATION_CHANNEL_USERNAME
    VERIFICATION_CHANNEL_ID = Config.VERIFICATION_CHANNEL_ID    
    ADMINS=Config.ADMINS
    NETWORK_IMG=Config.NETWORK_IMG
    HQ_ID=Config.HQ_ID

app=Client(
    "VERIFICATION-BOT",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=TOKEN,
    plugins=dict(root="NetworkVerificationBot/plugins")
     )
LOG.info("starting the bot....")
