import os

class Config:
    API_ID=16191628
    API_HASH="7d5acccaf1df4f5b7a690b203fd1953e"
    TOKEN="5651385902:AAFwigsgZLEETFCXutMjLyfMNgwuaUjMTIU"
    TOS_LINK="https://t.me/c/1547036942/1021"
    VERIFICATION_CHANNEL_ID=-1001715350671
    NETWORK_NAME = "ok"
    HQ_USERNAME = "ok"
    NETWORK_USERNAME = "ok"
    VERIFICATION_CHANNEL_USERNAME = "ok"
    ADMINS = list(int(x) for x in os.environ.get("ADMINS", "5264285143 1937701729").split(" "))
    NETWORK_IMG="https://telegra.ph/file/2c7a09bff109deec3e305.jpg"
