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
    all_info = []
    for some_var in extracting_info()['list']:
        day_info = []
        day_info.append(datetime.datetime.fromtimestamp(some_var['dt']).
                         strftime('%d-%m-%Y'))
        day_info.append(str(some_var['temp']['day']))
        day_info.append(str(some_var['feels_like']['day']))
        day_info.append(str(some_var['temp']['night']))
        all_info.append(day_info)
    return all_info


def creating_a_text_file():
    with open(f'{corr_info()[0][0]}-{city}-{days}-days-weather-forecast.txt',
              'w') as file:
        file.write('Date'.ljust(20) + 'Day temperature'.ljust(20) +
                'Feels like'.ljust(20) + 'Night temperature'.ljust(20) + '\n')
        for line in corr_info():
            for i, val in enumerate(line):
                line[i] = val.ljust(20)
            file.write(''.join(line) + '\n')


creating_a_text_file()
