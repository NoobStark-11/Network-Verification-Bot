from NetworkVerificationBot import app
from pyrogram import filters 
from pyrogram.types import (
    InlineKeyboardButton, 
    InlineKeyboardMarkup,
    CallbackQuery 
    )
VERIFY_MSG="""
Hello, In order to verify yourself, Are you accepting our Tos (Terms of Service)?
"""
VERIFY_BUTTONS= [
         [
           InlineKeyboardButton (text="yes i accept",callback_data="yes_verify")
         ],
         [
          InlineKeyboardButton (text="no,i decline",callback_data="no_verify")        
         ],
      ]
@app.on_message(filters.command("verify"))
async def verify(_,msg):
    await msg.reply_text(VERIFY_MSG,
      reply_markup=InlineKeyboardMarkup(VERIFY_BUTTONS)
      )

@app.on_callback_query()
async def _callback(_,CallbackQuery):
    query = CallbackQuery.message 
    if query == "yes_verify":
        await query.edit_text("hii")
