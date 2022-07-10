# 2. Написать функцию которая будет частично скрывать e-mail, пример:
# hide_email(somebody_email@gmail.com) -> em***@**il.com

import random

user_email = input("Please enter your email: ")
# Variant 1


def hidden_email(email: str) -> str:
    """This function will return email with "***" in last part of name part and
                                with "**" in first part of contracts part"""
    return user_email.split('@')[0][:-3] + "***@**" + \
                                           user_email.split('@')[1][2:]


print(hidden_email(user_email))

# Variant 2


def hidden_email_1(email: str, qty_of_asterix: int) -> str:
    """This function will return email with random symbols replaced
                                                                with "*"."""
    index = [key for key, value in enumerate(email) if not value == '@']
    rand_index = random.sample(index, qty_of_asterix)
    lst = list(email)
    for ind in rand_index:
        lst[ind] = '*'
    return "".join(lst)


print(hidden_email_1(user_email, 10))
