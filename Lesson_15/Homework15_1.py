# 1. Формат украинских номеров:
#    ВН1010НС или АА1010АА
# На ввод программа получает строку, в ответ должна вернуть является строка
# автомобильным номером или нет.
# * доп. Должна вернуть регион (должна знать регионы 2004 и 2013 гг.)
# Должна одинаково воспринимать AI - англ и АІ - украинский варианты.
# (для BI, AI, IA и т.д.)
import re
import csv

user_number = input('Please enter number: ').upper().\
    translate(str.maketrans('ABEIKMHOPCTX', 'АВЕІКМНОРСТХ'))
# Variant 1


def check_format(number: str):
    return True if re.fullmatch(r'\w{2}\d{4}\w{2}', number) else False


def check_region(number: str):
    with open('ua_auto.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if number[:2] in row['Code 2004'] or number[:2] \
                    in row['Code 2013']:
                return f'This number is registered in {row["Region"]}'


def check_number(number: str):
    if bool(check_region(number)) and check_format(number) is True:
        return check_region(number)
    else:
        return f'The format of this number is not correct for Ukraine'


print(check_number(user_number))
# Variant 2


def check_number2(number: str):
    if re.fullmatch(r'\w{2}\d{4}\w{2}', number):
        with open('ua_auto.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if number[:2] in row['Code 2004'] or number[:2] \
                        in row['Code 2013']:
                    return f'This number is registered in {row["Region"]}'
            else:
                return f'The format of this number is not correct for Ukraine'
    else:
        return f'The format of this number is not correct for Ukraine'


print(check_number2(user_number))
# Variant 3


def check_format(*args: str):
    return True if re.fullmatch(r'\w{2}\d{4}\w{2}', *args) else False


def check_number3(number: str):
    if check_format(number) is True:
        with open('ua_auto.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if number[:2] in row['Code 2004'] or number[:2] \
                        in row['Code 2013']:
                    return f'This number is registered in {row["Region"]}'
            else:
                return f'The format of this number is not correct for Ukraine'
    else:
        return f'The format of this number is not correct for Ukraine'


print(check_number3(user_number))
