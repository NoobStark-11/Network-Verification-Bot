from pyromod import listen
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
    await query.edit_text("click on /continue to proceed")
        
      
@app.on_callback_query(filters.regex("no_verify"))
async def nope(_, CallbackQuery):
    query=CallbackQuery.message
    await query.edit_text("please consider to come back again")
  

@app.on_message(filters.command("continue"))
async def verify(client,msg):
    id=msg.chat.id
    a = await client.ask(id,"Mind putting our tag on your name?")
    await msg.reply_text(f" {a.text} great")

@app.on_message(filters.command("poll"))
async def poll(client, message):
    x=message.chat.id
    a = await client.ask(x,"how many queries")
    xx =await client.ask(x,"poll1 query")
    xxx = await client.ask(x,"poll 1 query")    
    await app.send_poll(x,"is it a poll?",[f"{xx.text}",f"{xxx.text}"])
 
