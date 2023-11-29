import random
import datetime as dt

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

r_help ='I am a simple bot, my list of commands are: hello, roll, !help'


