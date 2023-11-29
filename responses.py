import random
import datetime

def handle_response(message) -> str:
    p_message = message.lower()
    
    if p_message == 'hello':
        return 'Hey there!'
    
    if p_message == 'roll':
        return str(random.randint(1,20))

    if p_message =='!help':
        return r_help
    
    if p_message =='date':
        return str(datetime.datetime.today())
    
    # if the input does not have any valid response
    return 'I dont understand what you are saying'

r_help ='I am a simple bot, my list of commands are: hello, roll, !help'


