from NetworkVerificationBot import app

async def info(_,msg):
    async with app:
        first_name = msg.from_user.first_name
        username = msg.from_user.username
        user_id = msg.from_user.id
        dc_id = msg.from_user.dc_id
