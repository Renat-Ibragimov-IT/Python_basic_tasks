# 3. Получить прогноз погоды для Одессы на следующие 5 дней и записать в файл
# с именем текущей даты,
# http://api.openweathermap.org/data/2.5/forecast/daily?q=city&cnt=1&units=
# metric&appid=f9ada9efec6a3934dad5f30068fdcbb8
# Параметр cnt = количество дней
# Параметр q = город
# Так мы получим и обработаем дату из ответа (ключ dt):
# datetime.datetime.fromtimestamp(1600419600)
# Применив к полученному обьекту даты strftime("%d-%m-%Y") получим строковую
# дату для записи в файл.
# Пример имени файла: 19-09-2020-Odessa-5-days-weather-forecast.txt
# Записанный файл должен выглядеть вот так:
#   Дата             Температура днем   По ощущениям
#   18-09-2020       17.86              11.18
#   19-09-2020       15.75              11.21
#   20-09-2020       20.37              17.49
#   21-09-2020       20.75              18.08
#   22-09-2020       20.96              17.47
# * доп. предоставить пользователю выбор города и количества дней,
# а также добавить колонку Температура ночью

import requests
import datetime

city = input('Please enter your city: ')
days = int(input('Please indicate for how many days '
                 'You want to check weather: '))
API_KEY = 'f9ada9efec6a3934dad5f30068fdcbb8'


def creating_text_file():
    forecast = requests.get('https://api.openweathermap.org/data/2.5/forecast/'
                            'daily?&units=metric', params={"q": city,
                             "cnt": days, 'appid': API_KEY}).json()
    dates_list = []
    day_temp = []
    feels_like = []
    night_temp = []
    for some_var in forecast['list']:
        dates_list.append(datetime.datetime.fromtimestamp(some_var['dt']).
                         strftime('%d-%m-%Y'))
        day_temp.append(str(some_var['temp']['day']))
        feels_like.append(str(some_var['feels_like']['day']))
        night_temp.append(str(some_var['temp']['night']))
    with open(f'{dates_list[0]}-{city}-{days}-days-weather-forecast.txt',
              'w') as file:
        file.write('Date'.ljust(20) + 'Day temperature'.ljust(20) +
                'Feels like'.ljust(20) + 'Night temperature'.ljust(20) + '\n')
        for var in range(int(days)):
            file.write(dates_list[var].ljust(20) + day_temp[var].ljust(20) +
                       feels_like[var].ljust(20) + night_temp[var] + '\n')


creating_text_file()
