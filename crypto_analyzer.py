# Da rimuovere per la versione 1.0
import os 
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('API_KEY')
######################################

import requests 

print('Welcome\n')

crypto_list = []

def input_crypto():
    while True:
        crypto = input(
            'Which crypto do you want to trace? (ex. bitcoin, ethereum...).' \
                'When you have done type "ok" to continue or "q" to quit the '
                    'program.\n'
            )
        url = f'https://api.coingecko.com/api/v3/coins/{crypto}'

        params = {
            'tickers': 'false',
            'market_data': 'false',
            'community_data': 'false',
            'developer-data': 'false',
            'sparkline': 'false'
        }

        headers = {
            'x-cg-demo-api-key': api_key
        }

        response = requests.get(url, params=params, headers=headers)
        if response.status_code == 200:
            if crypto == 'ok':
                return crypto_list
            elif crypto == 'q':
                print('Bye!')
                break
            else:        
                crypto_list.append(crypto)
        elif response.status_code == 404:
            print('The crypto id that you provided is not available, if it exists please remember to use lowercase letters.')

def input_quote_currency():
    while True:
        quote_currency = input(
            'Now please type the quote currency (ex. usd, eur...) or type "q" to ' \
                'quit the program.\n')
        
        url = 'https://api.coingecko.com/api/v3/simple/supported_vs_currencies'

        headers = {
            'x-cg-demo-api-key': api_key
        }

        response = requests.get(url, headers=headers).json()
        if quote_currency in response:
            if quote_currency == 'q':
                print('Bye!')
                break
            else:
                return quote_currency
        elif quote_currency not in response:
            print('The quote currency that you provided is not available, if it exists please remember to use lowercase letters.')

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