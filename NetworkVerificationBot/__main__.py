from pyrogram import filters
from NetworkVerificationBot import app, START_IMG,NETWORK_NAME,HQ_USERNAME, APPROVED_CHANNEL_USERNAME,NETWORK_USERNAME
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 
from pyrogram.errors import UserNotParticipant

START_MSG="""
ʜᴇʏ **{}**, ɪ ᴀᴍ {} ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ ʙᴏᴛ,
ᴀᴍ ʜᴇʀᴇ ᴛᴏ ᴠᴇʀɪғʏ ʏᴏᴜ ɪɴ ᴍʏ ɴᴇᴛᴡᴏʀᴋ.
ɪғ ʏᴏᴜ ᴀʀᴇ ʀᴇᴀᴅʏ ᴛᴏ ɢᴇᴛ ᴠᴇʀɪғɪᴇᴅ ɪɴ ᴏᴜʀ ɴᴇᴛᴡᴏʀᴋ 
ᴋɪɴᴅʟʏ ᴜsᴇ /verify ᴛᴏ ᴠᴇʀɪғʏ ʏᴏᴜʀsᴇʟғ.
"""

buttons = [
     [
       InlineKeyboardButton (text="ʜᴇᴀᴅǫᴜᴀᴛᴇʀs",url=f"https://t.me/{HQ_USERNAME}"),
       InlineKeyboardButton (text="ᴀᴘᴘʀᴏᴠᴇᴅ ғᴏʀᴍs",url=f"https://t.me/{APPROVED_CHANNEL_USERNAME}")
     ],
     [
       InlineKeyboardButton (text="ɴᴇᴛᴡᴏʀᴋ",url=f"https://t.me/{NETWORK_USERNAME}")
     ],
     ]


@app.on_message(filters.command("start"))
async def start(_, msg):
    try:
        await app.get_chat_member(-1001547036942,msg.from_user.id)
    except UserNotParticipant:
        await msg.reply_text("join our chat first", reply_markup=InlineKeyboardMarkup (buttons))
    return
    if msg.chat.type == "private":
        await app.send_photo(msg.from_user.id,
         photo=START_IMG,
         caption=START_MSG.format(msg.from_user.first_name, NETWORK_NAME),
            reply_markup=InlineKeyboardMarkup (buttons)
            )    
                
    else:
        await app.send_message(msg.from_user.id,"hey")        

if __name__ == "__main__" :
    app.run()
