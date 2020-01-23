import requests
import json
import misc
import re
from flask_sslify import SSLify
from flask import jsonify
from flask import request
from flask import Flask


app = Flask(__name__)
sslify = SSLify(app)
token = misc.Token
URL = "https://api.telegram.org/bot" + token + "/"


def write_json(data, filename="answer.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def send_message(chat_id, text="awaiting"):
    url = URL + "sendmessage"
    answer = {"chat_id": chat_id,
              "text": text}
    response = requests.post(url, json=answer)
    return response.json()


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
        return price
    elif crypto == "/dogecoin":
        url = 'https://yobit.net/api/3/ticker/doge_usd'
        r = requests.get(url).json()
        price = r["doge_usd"]["last"]
        return price
    elif crypto == "/litecoin":
        url = 'https://yobit.net/api/3/ticker/ltc_usd'
        r = requests.get(url).json()
        price = r["ltc_usd"]["last"]
        return price


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        r = request.get_json()
        chat_id = r["message"]["chat"]["id"]
        message = r["message"]["text"]
        pattern = r'/\w+'

        if re.search(pattern, message):
            price = get_price(parse_string(message))
            send_message(chat_id, text=price)


        return jsonify(r)
    return "<h1>awaiting</h1>"




if __name__ == "__main__":
    app.run()