# Написать приложение "Онлайн конвертер валют". =)
# Приложение спрашивает пользователя:
#    currency_from: string
#    currency_to: string
# Проверка ввода параметра валют (from, to) должна быть в symbols.json по ключу
# symbols)
#    amount: float
#    start_date: string
# (пример. 2020-09-22 если дата не в этом формате, выставлять по-умолчанию дату
# текущего дня, если дата превышает текущий день, тоже выставляем дату текущего
# дня)
#    Если дата меньше или равна текущему дню, то от start_date до текущего идет
# итерация:
# Приложение делает GET запрос:
# https://api.exchangerate.host/convert
# Принимаемые параметры from, to, amount, date
# (from=USD&to=UAH&amount=10000.5&date=2020-09-18)
# Итоговый вывод должен быть точно в таком же формате (пример если start_date
# == 2020-09-18):
# [['date', 'from', 'to', 'amount', 'rate', 'result'],
# ['2020-09-18', 'USD', 'UAH', 10000.5, 28.163466, 281648.743085],
# ['2020-09-19', 'USD', 'UAH', 10000.5, 28.163466, 281648.737791],
# ['2020-09-20', 'USD', 'UAH', 10000.5, 28.163455, 281648.630637],
# ['2020-09-21', 'USD', 'UAH', 10000.5, 28.23733, 282387.419415],
# ['2020-09-22', 'USD', 'UAH', 10000.5, 28.265772, 282671.854989]]
# ** доп. задание. ввод данных должен приниматься парсингом аргументов, модуль
# argparse.
# Только --start_date опциональный параметр.
# В итоге чтобы была возможность запустить приложение командой:
# python exchange_rates.py USD UAH 100 --start_date 2020-09-18
# В данном случае пользователя спрашивать не нужно.

import argparse
import datetime
import time
import json
import requests

URL = 'https://api.exchangerate.host/convert'


def initial_check():
    with open('symbols.json', 'r') as file:
        symbols_list = json.load(file)['symbols']
        if args.currency_from not in symbols_list:
            print('Please enter correct currency_from')
        elif args.currency_to not in symbols_list:
            print('Please enter correct currency_to')
        else:
            return extract_info()


def correct_dates():
    try:
        initial_date = datetime.datetime.strptime(args.start_date,
                                                  '%Y-%m-%d').date()
    except ValueError and TypeError:
        return datetime.datetime.utcnow().date()
    if initial_date > datetime.datetime.utcnow().date():
        return datetime.datetime.utcnow().date()
    else:
        return initial_date


def extract_info():
    user_date = correct_dates()
    info_list = [['date', 'from', 'to', 'amount', 'rate', 'result']]
    while user_date <= datetime.datetime.utcnow().date():
        request = requests.get(URL, params={'from': args.currency_from,
                                            'to': args.currency_to,
                                            'amount': args.amount,
                                            'date': user_date}).json()
        daily_info = [request['date'], request['query']['from'],
                      request['query']['to'], request['query']['amount'],
                      request['info']['rate'], request['result']]
        user_date += datetime.timedelta(days=1)
        info_list.append(daily_info)
        time.sleep(0.2)
    print('\n'.join(map(str, info_list)))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Online currency exchange')
    parser.add_argument('currency_from', nargs='?', default='USD', type=str)
    parser.add_argument('currency_to', nargs='?', default='UAH', type=str)
    parser.add_argument('amount', type=float)
    parser.add_argument('-sd', '--start_date', nargs='?',
                        default=datetime.datetime.utcnow().date())
    args = parser.parse_args()


initial_check()


