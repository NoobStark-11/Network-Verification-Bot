from pyrogram import filters
from NetworkVerificationBot import app, NETWORK_IMG,NETWORK_NAME,HQ_USERNAME,NETWORK_USERNAME,ADMINS,HQ_ID
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
       
     ],
     [
       InlineKeyboardButton (text="ɴᴇᴛᴡᴏʀᴋ",url=f"https://t.me/{NETWORK_USERNAME}")
     ],
     ]

HQ=[
     [
       InlineKeyboardButton (text="ʜᴇᴀᴅǫᴜᴀᴛᴇʀs",url=f"https://t.me/{HQ_USERNAME}"),       
     ],     
     ]

@app.on_message(filters.command("start") & filters.private)
async def start(_, msg):
    try:
       await msg._client.get_chat_member(HQ_ID, msg.from_user.id)
    except UserNotParticipant:
       await app.send_message(
			chat_id=msg.from_user.id,
			text=f"""
ʜᴇʏ {msg.from_user.mention},
ʏᴏᴜ ᴅɪᴅɴ'ᴛ ᴊᴏɪɴᴇᴅ ᴍʏ HQ.
ᴊᴏɪɴ ɪᴛ ᴛᴏ ᴜsᴇ ᴍᴇ..
""")
       return
    if msg.from_user.id in ADMINS:
        await msg.reply_text("ʜᴏᴡ ᴄᴀɴ ɪ ᴠᴇʀɪғʏ ᴀ ᴀᴅᴍɪɴ ? \nʏᴏᴜ ᴀʀᴇ ᴀʟʀᴇᴀᴅʏ ᴏᴜʀ ɴᴇᴛᴡᴏʀᴋ ᴍᴇᴍʙᴇʀ.")
    else:
        await app.send_photo(msg.from_user.id,
         photo=NETWORK_IMG,
         caption=START_MSG.format(msg.from_user.first_name, NETWORK_NAME),
            reply_markup=InlineKeyboardMarkup (buttons)
            )    
                                       
    

if __name__ == "__main__" :
    app.run()
