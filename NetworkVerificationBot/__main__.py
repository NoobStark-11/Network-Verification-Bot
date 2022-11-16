from pyrogram import filters
from NetworkVerificationBot import app, NETWORK_IMG

START_MSG="""
HEY THIS IS A VERIFICATION FORM
click /verify to verify yourself in our network 
"""
buttons= 
     [
     [
       InlineKeyboardButton (text="headquarters",url="https://t.me/+lUUS9nd1HxozYjBl")
       InlineKeyboardButton (text="approved forms",url="https://t.me/+lUUS9nd1HxozYjBl")
     ]
     [
       InlineKeyboardButton (text="network",url="https://t.me/+lUUS9nd1HxozYjBl")
     ]
     ]


@app.on_message(filters.command("start") & filters.private)
async def start(_, msg):
    await msg.reply_photo(
            photo=NETWORK_IMG,
            caption=START_MSG,
            reply_markup=InlineKeyboardMarkup (buttons)
            )

if __name__ == "__main__" :
    app.run()
