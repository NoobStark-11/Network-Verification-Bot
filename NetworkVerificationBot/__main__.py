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
       await msg._client.get_chat_member(-1001547036942, msg.from_user.id)
    except UserNotParticipant:
       await app.send_message(
			chat_id=msg.from_user.id,
			text=f"""
ʜᴇʏ {msg.from_user.mention},
ʏᴏᴜ ᴅɪᴅɴ'ᴛ ᴊᴏɪɴᴇᴅ ᴍʏ HQ.
ᴊᴏɪɴ ɪᴛ ᴛᴏ ᴜsᴇ ᴍᴇ..
""")
       return
    
    await app.send_photo(msg.from_user.id,
         photo=START_IMG,
         caption=START_MSG.format(msg.from_user.first_name, NETWORK_NAME),
            reply_markup=InlineKeyboardMarkup (buttons)
            )                                   
    

if __name__ == "__main__" :
    app.run()
