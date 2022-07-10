# Given a list of random integers. Replace all odd numbers in the list with
# zeros. And output their number.
import random


def initial_list_creation() -> list:
    """This function will create list with 10 random numbers"""
    initial_list = []
    for amount in range(10):
        initial_list.append(random.randrange(1, 1001))
    return initial_list


some_list = initial_list_creation()


def new_list_creation(user_list: list) -> tuple:
    """This function will replace all odd numbers to "0" and calculate amount
    of odd numbers"""
    replace_list = []
    for num in user_list:
        if num % 2 == 0:
            replace_list.append(num)
        else:
            replace_list.append(num * 0)
    corrected_list = list(num for num in replace_list if num == 0)
    return user_list, replace_list, len(corrected_list)


print(f'Random numbers list: {new_list_creation(some_list)[0]}')
print(f'List with replaced odd number: {new_list_creation(some_list)[1]}')
print(f'Amount of odd numbers: {new_list_creation(some_list)[2]}')
