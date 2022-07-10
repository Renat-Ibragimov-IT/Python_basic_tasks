# There is a json file. Write a program that will read it and calculate
# the total duration of all the tracks on the album.
# Basic case - will return the number of seconds.
# * Return hours:minutes:seconds as a string. Example: '0:41:39'

import datetime
import json


def rock_legends():
    """This function will read the given json file and return total
    tracks duration"""
    with open('/home/renat-ibragimov-it/acdc.json', 'r') as back_in_black:
        list_of_seconds = [int(seconds['duration']) for seconds in
                           json.load(back_in_black)['album']['tracks'][
                               'track']]
        return sum(list_of_seconds), \
               datetime.timedelta(seconds=sum(list_of_seconds))


print(f'Total seconds: {rock_legends()[0]}')
print(f'Total time: {rock_legends()[1]}')
