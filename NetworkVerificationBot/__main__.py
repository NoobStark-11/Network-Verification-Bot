from pyrogram import filters
from NetworkVerificationBot import app, NETWORK_IMG,NETWORK_NAME,HQ_USERNAME, PUBLIC_APPROVED_CHANNEL_USERNAME
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 

START_MSG="""
ʜᴇʏ {} ɪ ᴀᴍ {} ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ ʙᴏᴛ,
ᴀᴍ ʜᴇʀᴇ ᴛᴏ ᴠᴇʀɪғʏ ʏᴏᴜ ɪɴ ᴍʏ ɴᴇᴛᴡᴏʀᴋ.
ɪғ ʏᴏᴜ ᴀʀᴇ ʀᴇᴀᴅʏ ᴛᴏ ɢᴇᴛ ᴠᴇʀɪғɪᴇᴅ ɪɴ ʏᴏᴜʀ ɴᴇᴛᴡᴏʀᴋ 
ᴋɪɴᴅʟʏ ᴜsᴇ /verify ᴛᴏ ᴠᴇʀɪғʏ ʏᴏᴜʀsᴇʟғ.
"""

buttons = [
     [
       InlineKeyboardButton (text="ʜᴇᴀᴅǫᴜᴀᴛᴇʀs",url="https://t.me/+lUUS9nd1HxozYjBl"),
       InlineKeyboardButton (text="ᴀᴘᴘʀᴏᴠᴇᴅ ғᴏʀᴍs",url="https://t.me/+lUUS9nd1HxozYjBl")
     ],
     [
       InlineKeyboardButton (text="ɴᴇᴛᴡᴏʀᴋ",url="https://t.me/+lUUS9nd1HxozYjBl")
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
