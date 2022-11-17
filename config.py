import os

class Config:
    API_ID=
    API_HASH=""
    TOKEN=""
    TOS_LINK=""
    VERIFICATION_CHANNEL_ID=
    NETWORK_NAME = ""
    HQ_USERNAME = ""
    NETWORK_USERNAME = ""
    VERIFICATION_CHANNEL_USERNAME = ""
    ADMINS = list(int(x) for x in os.environ.get("ADMINS", "").split(" "))
    NETWORK_IMG=""
    HQ_ID=
