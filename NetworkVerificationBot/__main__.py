from pyrogram import filters
from NetworkVerificationBot import app, START_IMG,NETWORK_NAME,HQ_USERNAME, APPROVED_CHANNEL_USERNAME,NETWORK_USERNAME
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 

START_MSG="""
ʜᴇʏ {} ɪ ᴀᴍ {} ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ ʙᴏᴛ,
ᴀᴍ ʜᴇʀᴇ ᴛᴏ ᴠᴇʀɪғʏ ʏᴏᴜ ɪɴ ᴍʏ ɴᴇᴛᴡᴏʀᴋ.
ɪғ ʏᴏᴜ ᴀʀᴇ ʀᴇᴀᴅʏ ᴛᴏ ɢᴇᴛ ᴠᴇʀɪғɪᴇᴅ ɪɴ ʏᴏᴜʀ ɴᴇᴛᴡᴏʀᴋ 
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


@app.on_message(filters.command("start") & filters.private)
async def start(_, msg):
    await msg.reply_photo(
            photo=START_IMG,
            caption=START_MSG.format(msg.from_user.first_name, NETWORK_NAME),
            reply_markup=InlineKeyboardMarkup (buttons)
            )

if __name__ == "__main__" :
    app.run()
