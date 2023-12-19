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
    data = response.json()['Time Series (Daily)']
    data_list = [value for (key, value) in data.items()]

    #get yesterday's closing price
    yesterday_data = data_list[0]
    y_closing_price = yesterday_data['4. close']

    #the day before yesterday's closing price
    day_before_yesterday_data = data_list[1]
    d_b_y_closing_price = day_before_yesterday_data['4. close']

    #Calculate the percentage difference between the 2 prices
    difference = abs(float(y_closing_price) - float(d_b_y_closing_price))
    diff_percentage = (difference / float(y_closing_price)) * 100


    print(diff_percentage)


if __name__ == '__main__':
    main()