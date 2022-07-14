# Write a function that will partially hide the e-mail, for example:
# hide_email(somebody_email@gmail.com) -> em***@**il.com

import random

user_email = input("Please enter your email: ")


def hidden_email(email: str, qty_of_asterix: int) -> str:
    """This function will return email with random symbols replaced
                                                                with "*"."""
    index = [key for key, value in enumerate(email) if not value == '@']
    rand_index = random.sample(index, qty_of_asterix)
    lst = list(email)
    for ind in rand_index:
        lst[ind] = '*'
    return "".join(lst)


print(hidden_email(user_email, 10))
