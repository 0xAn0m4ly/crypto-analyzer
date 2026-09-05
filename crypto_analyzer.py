# Da rimuovere per la versione 1.0
import os 
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('API_KEY')
######################################

import requests 
import sys

print('Welcome...')

crypto_list = []

def input_crypto():
    while True:
        crypto = input(
            'Which crypto do you want to trace? (ex. bitcoin, ethereum...). ' \
                'When you have done type "ok" to continue or "q" to quit the '
                    'program.\n'
            )

        if crypto == 'q':
            print('Bye!')
            sys.exit()
        elif crypto == 'ok' and crypto_list:
             return crypto_list
        else:
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

            try:
                response = requests.get(url, params=params, headers=headers)
            except requests.exceptions.ConnectionError:
                print('Something is not working, check your internet connection or your API key and try again.')
                sys.exit()
            else:
                if response.status_code == 200:        
                    crypto_list.append(crypto)
                elif response.status_code == 404:
                    print('The crypto id that you provided is not available, if it exists please remember to use lowercase letters.')


def input_quote_currency():

    print('---------------------------')

    while True:
        quote_currency = input(
            'Now please type the quote currency (ex. usd, eur...) or type "q" to ' \
                'quit the program.\n'
            )

        if quote_currency == 'q':
            print('Bye!')
            sys.exit()
        else:
        
            url = 'https://api.coingecko.com/api/v3/simple/supported_vs_currencies'

            headers = {
                'x-cg-demo-api-key': api_key
            }

            try:
                response = requests.get(url, headers=headers).json()
            except requests.exceptions.ConnectionError:
                print('Something is not working, check your internet connection or your API key and try again.')
                sys.exit()
            else:
                if quote_currency in response:
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

        try:
            request = requests.get(url, params=params, headers=headers)
        except requests.exceptions.ConnectionError:
            print('Something is not working, check your internet connection or your API key and try again.')
            sys.exit()
        else:
            data = request.json()
            for crypto_id in data.values():
                for value in crypto_id.values():
                    print(f'- 1 {crypto} now is {value} {quote_currency}')

get_data()