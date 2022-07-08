# 7. Написать функцию `is_date`,
# принимающую 3 аргумента — день, месяц и год.
# Вернуть `True`, если дата корректная (надо учитывать число месяца.
# Например 30.02 - дата не корректная, так же 31.06 или 32.07 и т.д.),
# и `False` иначе. (можно использовать модуль calendar или datetime)

import datetime
day = int(input("Please enter day of the month: "))
month = int(input("Please enter month: "))
year = int(input("Please enter year: "))


def is_date(day: int, month: int, year: int):
    try:
        datetime.datetime(day=day, month=month, year=year)
        return True
    except ValueError:
        return False


print(is_date(day, month, year))
