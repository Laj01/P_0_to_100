import requests

OWM_ENDPOINT = 'https://api.openweathermap.org/data/2.5/forecast'
API_KEY = '1c3407d48d263bfca63fe47715a25f7a'

def main():

    weather_params = {
        'lat': 47.319114,
        'lon': 21.093732,
        'appid': API_KEY,
    }

    response = requests.get(OWM_ENDPOINT, params=weather_params)
    print(response.status_code)


if __name__ == '__main__':
    main()