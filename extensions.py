import requests
import json
from config import *


class ConvertionException(Exception):
    pass


class Converter:
    def convert(quote: str, base: str, amount: str):
        try:
            quote_ticker = exch[quote]
        except KeyError:
            raise ConvertionException(f'Я не знаю такой валюты - "{quote}", проверь верное название через /values')
        try:
            base_ticker = exch[base]
        except KeyError:
            raise ConvertionException(f'Я не знаю такой валюты - "{base}", проверь верное название через /values')
        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Укажи количество валюты в цифрах, - "{amount}" не подойдет.')
        if exch[quote] == exch[base]:
            raise ConvertionException(f'Зачем сравнивать одну и ту же валюту "{base}"?')
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        price = json.loads(r.content)[exch[base]]
        return price
