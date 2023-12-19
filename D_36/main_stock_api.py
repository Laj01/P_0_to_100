import requests


STOCK_API_KEY = 'HWYKJ6AH8I8EKSX8'
STOCK_ENDPOINT = 'https://www.alphavantage.co/query'
STOXK_SYMBOL = 'TSLA'

def main():
    stock_params = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': STOXK_SYMBOL,
        'apikey': STOCK_API_KEY,
    }

    response = requests.get(STOCK_ENDPOINT, params=stock_params)
    response.raise_for_status()
    print(response.json())


if __name__ == '__main__':
    main()