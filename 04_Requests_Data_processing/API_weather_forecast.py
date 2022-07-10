# Get the weather forecast for Odessa for the next 5 days and write it to a
# file with the name of the current date
# http://api.openweathermap.org/data/2.5/forecast/daily?q=city&cnt=1&uni
# metric&appid=f9ada9efec6a3934dad5f30068fdcbb8
# File name example: 19-09-2020-Odessa-5-days-weather-forecast.txt
# The filled file should look like this:
#   Date             Day temperature    Feels like
#   18-09-2020       17.86              11.18
#   19-09-2020       15.75              11.21
#   20-09-2020       20.37              17.49
#   21-09-2020       20.75              18.08
#   22-09-2020       20.96              17.47
# Optional: provide the user with a choice of city and number of days,
# and also add a column Temperature at night
import datetime

import requests

city = input('Please enter your city: ')
days = int(input('Please indicate for how many days '
                 'You want to check weather: '))
API_KEY = 'f9ada9efec6a3934dad5f30068fdcbb8'
URL = 'https://api.openweathermap.org/data/2.5/forecast/daily?&units=metric'


def extracting_info():
    """This function will extract all info from API"""
    return requests.get(URL, params={"q": city, "cnt": days,
                                     'appid': API_KEY}).json()


def corr_info():
    """This function will select the required information from
    all the information"""
    all_info = []
    for some_var in extracting_info()['list']:
        day_info = [datetime.datetime.fromtimestamp(some_var['dt']).
                    strftime('%d-%m-%Y'), str(some_var['temp']['day']),
                    str(some_var['feels_like']['day']),
                    str(some_var['temp']['night'])]
        all_info.append(day_info)
    return all_info


def creating_a_text_file():
    """Tis function will create a text file with requested info"""
    with open(f'{corr_info()[0][0]}-{city}-{days}-days-weather-forecast.txt',
              'w') as file:
        file.write('Date'.ljust(20) + 'Day temperature'.ljust(20) +
                   'Feels like'.ljust(20) + 'Night temperature'.ljust(
            20) + '\n')
        for line in corr_info():
            for i, val in enumerate(line):
                line[i] = val.ljust(20)
            file.write(''.join(line) + '\n')


creating_a_text_file()
