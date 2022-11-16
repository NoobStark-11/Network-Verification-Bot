from NetworkVerificationBot import app, NETWORK_IMG

START_MSG="""
HEY THIS IS A VERIFICATION FORM
"""

@app.on_message(filters.command(start))
async def start(_, msg):
    await msg.reply_photo(
            photo="NETWORK_IMG",
            caption=START_MSG
            )
if __name__ == "__main__" :
    app.run()
