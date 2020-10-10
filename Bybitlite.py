import logging
import requests
from requests import ConnectionError
import os

ENDPOINT = 'https://api.bybit.com'

#if the API id data is stored as enviroment variable (recommended method)
APIid = {'key': os.environ.get('BYBIT_KEY'),
         'secret': os.environ.get('BYBIT_SECRET')}

# if you want to hard code the API data directly (not recommended)
# APIid = {'key': "YOUR_API_KEY_HERE",
#          'secret': "YOUR_API_SECRET_HERE"}


# this module makes public calls to the Bybit REST API


def request(method, path, params=None):
    try:
        resp = requests.request(method, ENDPOINT + path, params=params)
        data = resp.json()
        if data["ret_msg"] != 'OK':
            logging.error(data['ret_msg'])
            return None
        else:
            return data['result']
    except ConnectionError as e:
        logging.error(e)


def tickers(symbol=''):
    """
    symbol: the currency symbol if left empty returns ticker of all symbols
    """
    path = '/v2/public/tickers'
    params = {
        'symbol': symbol,
    }

    data = request('GET', path, params)
    return data
