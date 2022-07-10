# Write an application "Online currency converter".
# The application asks the user:
#    currency_from: string
#    currency_to: string
# Checking the input of the currency parameter (from, to) should be in
# "symbols.json" by the symbols key)
#    amount: float
#    start_date: string
# (example: 2020-09-22 if the date is not in this format, set the default date
# of the current day, if the date is greater than the current day, also set the
# date of the current day)
# The application makes a GET request:
# https://api.exchangerate.host/convert
# Accepted parameters from, to, amount, date
# (from=USD&to=UAH&amount=10000.5&date=2020-09-18)
# The final output must be in exactly the same format:
# [['date', 'from', 'to', 'amount', 'rate', 'result'],
# ['2020-09-18', 'USD', 'UAH', 10000.5, 28.163466, 281648.743085],
# ['2020-09-19', 'USD', 'UAH', 10000.5, 28.163466, 281648.737791],
# ['2020-09-20', 'USD', 'UAH', 10000.5, 28.163455, 281648.630637],
# ['2020-09-21', 'USD', 'UAH', 10000.5, 28.23733, 282387.419415],
# ['2020-09-22', 'USD', 'UAH', 10000.5, 28.265772, 282671.854989]]
# Optional: input must be accepted by argument parsing, module argparse.
# Only --start_date is optional.
# As a result, to be able to run the application with the command:
# python exchange_rates.py USD UAH 100 --start_date 2020-09-18
# In this case, the user does not need to be asked.

import argparse
import datetime
import json
import time

import requests

URL = 'https://api.exchangerate.host/convert'


def initial_check():
    """This function will check the input parameters "currency_from" and
    "currency_to" """
    with open('symbols.json', 'r') as file:
        symbols_list = json.load(file)['symbols']
        if args.currency_from not in symbols_list:
            print('Please enter correct currency_from')
        elif args.currency_to not in symbols_list:
            print('Please enter correct currency_to')
        else:
            return extract_info()


def correct_dates():
    """This function will check if the entered date is correct"""
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
    """This function will extract all necessary info and return output"""
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
