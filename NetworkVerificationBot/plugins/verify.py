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
    full_name = await client.ask(id,"ᴡʜᴀᴛ ɪs ʏᴏᴜʀ ғᴜʟʟ ɴᴀᴍᴇ ?")
    age = await client.ask(id,"ʜᴏᴡ ᴏʟᴅ ᴀʀᴇ ʏᴏᴜ ?")
    gender = await client.ask(id,"ᴡʜᴀᴛ's ʏᴏᴜʀ ɢᴇɴᴅᴇʀ ?")
    channels = await client.ask(id,"ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴜsᴇʀɴᴀᴍᴇs")
    groups = await client.ask(id,"ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇs")
    bots = await client.ask(id,"ʏᴏᴜʀ ʙᴏᴛ ᴜsᴇʀɴᴀᴍᴇs")
    country = await client.ask(id,"ғʀᴏᴍ ᴡʜɪᴄʜ ᴄᴏᴜɴᴛʀʏ ʏᴏᴜ ʙᴇʟᴏɴɢ ᴛᴏ ?")
    skills = await client.ask(id,"ʜᴀᴠᴇ ᴀɴʏ sᴋɪʟʟ ?")
    github = await client.ask(id,"ʜᴀᴠᴇ ɢɪᴛʜᴜʙ ᴀᴄᴄᴏᴜᴛ..?\nɢɪᴠᴇ ᴍᴇ ᴛʜᴇ ʟɪɴᴋ")
    about = await client.ask(id,"ᴛᴇʟʟ ᴍᴇ sᴏᴍᴇᴛʜɪɴɢ ᴀʙᴏᴜᴛ ʏᴏᴜʀsᴇʟғ.")
    tag = await client.ask(id,"ᴄᴀɴ ʏᴏᴜ ᴘᴜᴛ ᴏᴜʀ ɴᴇᴛᴡᴏʀᴋ ᴛᴀɢ ᴏɴ ʏᴏᴜʀ ɴᴀᴍᴇ ?")
    reason = await client.ask(id,"ʜᴀᴠᴇ ᴀɴʏ  ʀᴇᴀsᴏɴ ᴛᴏ ᴊᴏɪɴɪɴɢ ᴏᴜʀ ɴᴇᴛᴡᴏʀᴋ, ɪғ ʜᴀᴠᴇ ᴛʜᴇɴ ᴡʀɪᴛᴇ ɪᴛ ᴅᴏᴡɴ.")    
    await app.send_message(VERIFICATION_CHANNEL_ID,
    f"""
 ❍═❰ 𝚅𝙴𝚁𝙸𝙵𝙸𝙲𝙰𝚃𝙸𝙾𝙽 𝙵𝙾𝚁𝙼 ❱═❍
◎ ─━──━─❖─━──━─ ◎
➻ **ғɪʀsᴛ ɴᴀᴍᴇ :** `{first_name}`
➻ **ᴜsᴇʀɴᴀᴍᴇ :** @{username}
➻ **ᴜsᴇʀ ɪᴅ :** `{user_id}`
➻ **ᴅᴄ ɪᴅ :** `{dc_id}`   
◎ ─━──━─❖─━──━─ ◎
➻ **ғᴜʟʟ ɴᴀᴍᴇ :** `{full_name.text}`
➻ **ᴀɢᴇ :** `{age.text}`
➻ **ɢᴇɴᴅᴇʀ :** `{gender.text}`
➻ **ᴄʜᴀɴɴᴇʟs :** {channels.text}
➻ **ɢʀᴏᴜᴘs :** {groups.text}
➻ **ʙᴏᴛs :** {bots.text}
➻ **ᴄᴏᴜɴᴛʀʏ** : `{country.text}`
◎ ─━──━─❖─━──━─ ◎
➻ **sᴋɪʟʟs :** `{skills.text}`
➻ **ɢɪᴛʜᴜʙ ʟɪɴᴋ :** {github.text}
➻ **ᴀʙᴏᴜᴛ :** `{about.text}`
➻ **ᴄᴀɴ ᴘᴜᴛ ɴᴇᴛᴡᴏʀᴋ's ᴛᴀɢ :** `{tag.text}`
➻ **ʀᴇᴀsᴏɴ :** `{reason.text}`
◎ ─━──━─❖─━──━─ ◎
""",
      reply_markup=InlineKeyboardMarkup (VERIFY_BUTTONS)
     )
    await msg.reply_text("ok")
    


 
