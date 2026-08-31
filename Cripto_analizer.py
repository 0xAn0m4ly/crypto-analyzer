# Da rimuovere per la versione 1.0
import os 
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('API_KEY')
######################################

import requests 

print('Welcome\n')
      
# Bisogna trovare un modo di accertare che la crypto inserita sia esistente
# magari tramite una richiesta get e poi mettere una lista e dire se sta qui fai
# i blocchi if seguenti

crypto_list = []

def input_crypto():
    while True:
        crypto = input(
            'Which crypto do you want to trace? (ex. bitcoin, ethereum...),' \
                'when you have done type "ok" to continue or "q" to quit the '
                    'program.\n'
            )
        if crypto == 'ok':
            return crypto_list
        elif crypto == 'q':
            print('Bye!')
            break
        else:        
            crypto_list.append(crypto)

# Lo stesso controllo vael anche per le valute di scambio

def input_quote_currency():
    while True:
        quote_currency = input(
            'Now please type the quote currency (ex. usd, eur...) or type "q" to ' \
                'quit the program.\n')
        if quote_currency == 'q':
            print('Bye!')
            break
        else:
            return quote_currency
