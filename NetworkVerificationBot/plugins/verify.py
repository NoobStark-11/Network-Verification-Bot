from NetworkVerificationBot import app
from pyrogram import filters 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup,CallbackQuery 
    
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

@app.on_callback_query(filters.regex("yes_verify"))
async def yos(_, CallbackQuery):
    query = CallbackQuery.message
    await query.edit_text("Mind putting our tag on your name?",
        reply_markup=InlineKeyboardMarkup (
         [
         [
          InlineKeyboardButton (text="yes i can",callback_data="yes_tag"),
          InlineKeyboardButton (text="no i can't ",callback_data="no_tag")
         ],
         ],
        ),
      )
      

@app.on_callback_query(filters.regex("no_verify"))
async def nope(_, CallbackQuery):
    query=CallbackQuery.message
    await query.edit_text("please consider to come back again")

@app.on_callback_query(filters.regex("yes_tag"))
async def yos(_, CallbackQuery):
    query = CallbackQuery.message
    await query.edit_text("great")
    
