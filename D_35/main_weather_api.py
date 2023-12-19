import requests


OWM_ENDPOINT = 'https://api.openweathermap.org/data/2.5/forecast'
API_KEY = '1c3407d48d263bfca63fe47715a25f7a'

def main():

    weather_params = {
        'lat': 47.319114,
        'lon': 21.093732,
        'cnt': 4,
        'appid': API_KEY,
    }

    is_raining = False
    response = requests.get(OWM_ENDPOINT, params=weather_params)
    response.raise_for_status()
    weather_data = response.json()
    #print(weather_data['list'][0]['weather'][0]['id'])
    for hour_data in weather_data['list']:
        code = hour_data['weather'][0]['id']
        if int(code) < 700:
            is_raining = True

    if is_raining:
        print('It will rain in the next 12 hours.')
    else:
        print('It will not rain in the next 12 hours.')
        

if __name__ == '__main__':
    main()