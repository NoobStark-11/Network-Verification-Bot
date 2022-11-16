import os
from NetworkVerificationBot import app, VERIFICATION_CHANNEL_ID,START_IMG as NETWORK_IMG
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
    first_name = msg.from_user.first_name
    username = msg.from_user.username
    user_id = msg.from_user.id
    dc_id = msg.from_user.dc_id
    last_online_date = msg.from_user.last_online_date 
    photo = msg.from_user.photo.big_file_id
    media =  await app.download_media(message=photo)
    
    a = await client.ask(id,"Mind putting our tag on your name?")
    b = await client.ask(id,"Write the reason(s) for joining our network.")
    c = await client.ask(id,"Your full name:")
    d = await client.ask(id,"Your Age:")
    e = await client.ask(id,"Your Gender:")
    f = await client.ask(id,"Country you belongs from?")
    g = await client.ask(id,"Your github link:")
    h = await client.ask(id,"Programming languages you know yet far are:")
    i = await client.ask(id,"Your channels usernames:")
    j = await client.ask(id,"Your groups usernames/links:")
    k = await client.ask(id,"Your bots usernames:")
    l = await client.ask(id,"Your skills:")
    m = await client.ask(id,"Tell me about yourself in one message:")
    await app.send_photo(VERIFICATION_CHANNEL_ID,NETWORK_IMG, 
    caption=f"""
╔════❰ 𝚅𝙴𝚁𝙸𝙵𝙸𝙲𝙰𝚃𝙸𝙾𝙽 𝙵𝙾𝚁𝙼 ❱═❍
║╭━━━━━━━━━━━━━━━➣
║┣⪼ **ғɪʀsᴛ ɴᴀᴍᴇ :**
║┣⪼ **ᴜsᴇʀɴᴀᴍᴇ :**
║┣⪼ **ᴜsᴇʀ ɪᴅ :**
║┣⪼ **ᴅᴄ ɪᴅ :**
║╰━━━━━━━━━━━━━━━➣   
   ╭━━━━━━━━━━━━━━━➣
║┣⪼ **ғᴜʟʟ ɴᴀᴍᴇ :**
║┣⪼ **ᴀɢᴇ :**
║┣⪼ **ɢᴇɴᴅᴇʀ :**
║┣⪼ **ᴄʜᴀɴɴᴇʟs :**
║┣⪼ **ɢʀᴏᴜᴘs :**
║┣⪼ **ʙᴏᴛs :**
║┣⪼ **ᴄᴏᴜɴᴛʀʏ :**
║╰━━━━━━━━━━━━━━━➣
   ╭━━━━━━━━━━━━━━━➣
║┣⪼ **sᴋɪʟʟs :**
║┣⪼ **ɢɪᴛʜᴜʙ ʟɪɴᴋ :**
║┣⪼ **ᴀʙᴏᴜᴛ :** 
║┣⪼ **ᴄᴀɴ ᴘᴜᴛ ɴᴇᴛᴡᴏʀᴋ's ᴛᴀɢ :**
║┣⪼ **ʀᴇᴀsᴏɴ :**
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍
""",
      reply_markup=InlineKeyboardMarkup (VERIFY_BUTTONS)
     )
    await msg.reply_text("ok")
    


 
