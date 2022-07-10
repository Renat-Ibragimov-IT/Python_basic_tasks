# Write a function that returns the current time.
# And wrap it in @countdown decorator which will count down 3 seconds.
# Example:
# >>> what_time_is_it_now()
# 3
# 2
# 1
# '16:21'

import time


def countdown(func):
    """This decorator will count down three seconds"""
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
    """This function will return current time"""
    return time.strftime('%H:%M')


what_time_is_it_now()
