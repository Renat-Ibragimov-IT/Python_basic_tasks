import requests
import datetime

city = input('Please enter your city: ')
days = int(input('Please indicate for how many days '
                 'You want to check weather: '))
API_KEY = 'f9ada9efec6a3934dad5f30068fdcbb8'
URL = 'https://api.openweathermap.org/data/2.5/forecast/daily?&units=metric'


def extracting_info():
    return requests.get(URL, params={"q": city, "cnt": days,
                                     'appid': API_KEY}).json()


def corr_info():
    dates_list = []
    day_temp = []
    feels_like = []
    night_temp = []
    for some_var in extracting_info()['list']:
        dates_list.append(datetime.datetime.fromtimestamp(some_var['dt']).
                         strftime('%d-%m-%Y'))
        day_temp.append(str(some_var['temp']['day']))
        feels_like.append(str(some_var['feels_like']['day']))
        night_temp.append(str(some_var['temp']['night']))
    return dates_list, day_temp, feels_like, night_temp


def creating_a_text_file():
    with open(f'{corr_info()[0][0]}-{city}-{days}-days-weather-forecast.txt',
              'w') as file:
        file.write('Date'.ljust(20) + 'Day temperature'.ljust(20) +
                'Feels like'.ljust(20) + 'Night temperature'.ljust(20) + '\n')
        for var in range(int(days)):
            file.write(corr_info()[0][var].ljust(20) +
                       corr_info()[1][var].ljust(20) +
                       corr_info()[2][var].ljust(20) +
                       corr_info()[3][var] + '\n')


creating_a_text_file()
