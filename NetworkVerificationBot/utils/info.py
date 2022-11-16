from NetworkVerificationBot import app

def info(_,msg):    
    first_name = msg.from_user.first_name
    username = msg.from_user.username
    user_id = msg.from_user.id
    dc_id = msg.from_user.dc_id
    return first_name,username,user_id,dc_id
        
