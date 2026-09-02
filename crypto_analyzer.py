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

def get_data():
    crypto_list = input_crypto()
    quote_currency = input_quote_currency()
    print('Getting data...\n')
    for crypto in crypto_list:
        url = 'https://api.coingecko.com/api/v3/simple/price'
        params = {
            'ids': crypto,
            'vs_currencies': quote_currency
        }
        headers = {
            'x-cg-demo-api-key': api_key
        }
        request = requests.get(url, params=params, headers=headers)
        data = request.json()
        for crypto_id in data.values():
            for value in crypto_id.values():
                print(f'- 1 {crypto} now is {value} {quote_currency}')

get_data()