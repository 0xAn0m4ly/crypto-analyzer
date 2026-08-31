# Da rimuovere per la versione 1.0
import os 
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('API_KEY')
######################################

import requests 

print('Welcome')
# Bisogna trovare un modo di accertare che la crypto inserita sia esistente
# magari tramite una richiesta get

crypto_list = []

def input_crypto():
    while True:
        crypto = input(
            'Which crypto do you want to trace? (ex. bitcoin, ethereum...),' \
            'when you have done type "ok" to continue or "q" to quit the program.'
            )
        if crypto == 'ok':
            return crypto_list
        elif crypto == 'q':
            break
        else:        
            crypto_list.append(crypto)

