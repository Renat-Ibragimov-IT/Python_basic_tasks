# 3. Вводимый пользователем пароль должен соответсвовать требованиям,
# 	1. Как минимум 1 символ от a-z
# 	2. Как минимум 1 символ от A-Z
# 	3. Как минимум 1 символ от 0-9
# 	4. Как минимум 1 символ из $#@-+=
# 	5. Минимальная длина пароля 8 символов.
# Программа принимает на ввод строку, в случае если пароль не верный -
# пишет какому требованию не соответствует и спрашивает снова,
# в случае если верный - пишет 'Password is correct'.
import re

user_password = input('Please enter Your password: ')
# Variant 1


def check_password(password: str):
    """This function will check password with many "if"=))"""
    if not re.search(r'[a-z]', password):
        print('Your password should contain at least one symbol "a-z"')
    if not re.search(r'[A-Z]', password):
        print('Your password should contain at least one symbol "A-Z"')
    if not re.search(r'\d', password):
        print('Your password should contain at least one digit')
    if not re.search(r'[$#@\-+=]', password):
        print('Your password should contain at least one special symbol')
    if not re.search(r'.{8,}', password):
        print('Your password length should be at least 8 symbols')
    else:
        return print('Your password is correct')


# Variant 2


def checks(password: str):
    """This function will check password without many "if"=)"""
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
checks(user_password)
