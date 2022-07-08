# 2. Написать функцию которая возвращает текущее время. И обернуть ее в
# декоратор @countdown который отсчитает 3 секунды.
# Пример:
# >>> what_time_is_it_now()
# 3
# 2
# 1
# '16:21'
# time.sleep() поможет программе уснуть на первый аргумент секунду =)
# Вернуть время поможет метод time.strftime, с аргументом '%H:%M'

import time


def countdown(func):

    def wrapper(*args, **kwargs):
        seconds = 3
        while seconds:
            print(seconds)
            seconds -= 1
            time.sleep(1)
        print(func(*args, **kwargs))
    return wrapper


@countdown
def what_time_is_it_now():
    return time.strftime('%H:%M')


what_time_is_it_now()
