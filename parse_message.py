import requests
import re
from main import write_json


def parse_string(text):
    pattern = r'/\w+'
    crypto = re.search(pattern, text).group()
    return crypto


def get_price(crypto):
    if crypto == "/bitcoin":
        url = 'https://yobit.net/api/3/ticker/btc_usd'
        r = requests.get(url).json()
        price = r["btc_usd"]["last"]
        return str(price) + " usd"
    elif crypto == "/ethereum":
        url = 'https://yobit.net/api/3/ticker/eth_usd'
        r = requests.get(url).json()
        price = r["eth_usd"]["last"]
        print (str(price) + " usd")
    elif crypto == "/dogecoin":
        url = 'https://yobit.net/api/3/ticker/doge_usd'
        r = requests.get(url).json()
        price = r["doge_usd"]["last"]
        print (str(price) + " usd")
    elif crypto == "/litecoin":
        url = 'https://yobit.net/api/3/ticker/ltc_usd'
        r = requests.get(url).json()
        price = r["ltc_usd"]["last"]
        print (str(price) + " usd")

def main():
    #print(get_price_btc())
    print(get_price(parse_string("цена /bitcoin?")))

if __name__ == "__main__":
    main()