import requests
import time
from datetime import datetime

BITCOIN_URL = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'
IFTTT_WEBHOOK_URL = 'https://maker.ifttt.com/trigger/{}/with/key/bL3iYn7YdX2PO7K2u9UaPE'
BITCOIN_PRICE_THRESHOLD = 8500


def get_bitcoin_price():
    response = requests.get(BITCOIN_URL)
    response_data = response.json()

    if response_data:
        return float(response_data[0]['price_usd'])


def post_ifttt_webhook(event, value):
    data = {'value1': value}
    requests.post(IFTTT_WEBHOOK_URL.format(event),json=data)


def format_price_history(price_history):
    rows = []

    for price in price_history:
        date_string = price['date'].strftime('%d.%m.%Y %H:%M')
        bitcoin_price = price['price']
        row = '{}: <b>{}</b>'.format(date_string, bitcoin_price)
        rows.append(row)

    return '<br>'.join(rows)


def main():
    price_history = []

    while True:
        price = get_bitcoin_price()
        now = datetime.now()
        price_history.append({'date': now, 'price': price})

        if price < BITCOIN_PRICE_THRESHOLD:
            post_ifttt_webhook('bitcoin_price_emergency', price)

        if len(price_history) == 5:
            post_ifttt_webhook('bitcoin_price_update', format_price_history(price_history))
            price_history = []

        time.sleep(2)


if __name__ == '__main__':
    main()

