# The password entered by the user must meet the requirements
# 1. At least 1 character from a-z
# 2. At least 1 character from A-Z
# 3. At least 1 character from 0-9
# 4. At least 1 character from $#@-+=
# 5. The minimum password length is 8 characters.
# The program accepts a string as input, if the password is not correct -
# it writes what requirement it does not meet, if it is correct
# - it writes 'Password is correct'.
import re

user_password = input('Please enter Your password: ')


def check_password(password: str):
    """This function will check if the entered password meets
    all requirements"""
    self_checks = {1: re.search(r'[a-z]', password),
                   2: re.search(r'[A-Z]', password),
                   3: re.search(r'\d', password),
                   4: re.search(r'[$#@\-+=]', password),
                   5: re.search(r'.{8,}', password)}
    errors = {1: 'Your password should contain at least one symbol "a-z"',
              2: 'Your password should contain at least one symbol "A-Z"',
              3: 'Your password should contain at least one digit',
              4: 'Your password should contain at least one special symbol',
              5: 'Your password length should be at least 8 symbols'}
    checklist = []
    for k, v in self_checks.items():
        if bool(v) is False:
            print(errors[k])
            checklist.append(k)
    if not checklist:
        print('Your password is correct')


check_password(user_password)
