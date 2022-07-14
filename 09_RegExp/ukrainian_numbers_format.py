# Format of Ukrainian numbers:
# ВН1010НС или АА1010АА
# On input, the program receives a string, in response it should return whether
# the string is a car number or not.
# * Optional: must return region (must know 2004 and 2013 regions)
# Should equally perceive AI - English and AI - Ukrainian variants
# (for BI, AI, IA, etc.)
import re
import csv

user_number = input('Please enter number: ').upper().\
    translate(str.maketrans('ABEIKMHOPCTX', 'АВЕІКМНОРСТХ'))


def check_format(*args: str):
    """This function will check if the format of the entered string matches
    the format of auto numbers"""
    return True if re.fullmatch(r'\w{2}\d{4}\w{2}', *args) else False


def check_number(number: str):
    """This function will check if the entered number is Ukrainian"""
    if check_format(number) is True:
        with open('ua_auto.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if number[:2] in row['Code 2004'] or number[:2] \
                        in row['Code 2013']:
                    return f'This number is registered in {row["Region"]}'
    else:
        return f'The format of this number is not correct for Ukraine'


print(check_number(user_number))
