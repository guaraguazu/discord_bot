import random



def handle_response(message) -> str:
    p_message = message.lower()
    
    if p_message == 'hello':
        return 'Hey there!'
    
    if p_message == 'roll':
        return str(random.randint(1,20))

    if p_message =='!help':
        return r_help
    
    # return 'I dont know what you said'

    return 'I dont understand'

options = ['Hello','Roll','!Help']
r_help = f'I am a limited bot, so far my options are: ', (for i in options: print(i))}


