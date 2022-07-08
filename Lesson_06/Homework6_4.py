# 4. Во вложении есть json файл. Написать программу которая прочитает его и
# посчитает общую длительность всех треков в альбоме.
# Базовый кейс - вернет количество секунд.
# * доп. усложнение вернуть в виде строки часы:минуты:секунды, прим. '0:41:39'
# (datetime.timedelta)

import json
import datetime


def rock_legends():
    with open('/home/renat-ibragimov-it/acdc.json', 'r') as back_in_black:
        list_of_seconds = [int(seconds['duration']) for seconds in
                        json.load(back_in_black)['album']['tracks']['track']]
        return sum(list_of_seconds), \
                              datetime.timedelta(seconds=sum(list_of_seconds))


print("Total seconds:", rock_legends()[0])
print("Total time:", rock_legends()[1])
