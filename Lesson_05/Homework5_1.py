# 1. Написать функцию `is_prime`, принимающую 1 аргумент — число от 0 до 1000,
#    и возвращающую `True`, если оно простое, и `False` - иначе.
# (Простые числа - те которые делятся без остатка только на само себя или 1,
#  например 2, 3, 5, 7, 11...)

def user_number(*args) -> int:
    number = int(input("Please enter number from 1 to 1000 to check if it is "
                       "a prime number: "))
    if 0 <= number <= 1000:
        return number
    else:
        print("Incorrect number")
    return user_number()


def is_prime_short(some_num: int) -> int:
    num = 2
    while some_num % num:
        num += 1
    return True if num == some_num else False


print(is_prime_short(user_number()))


def is_prime(some_num: int) -> int:
    user_numbers_range = list(range(2, some_num))
    prime_list = []
    for num in user_numbers_range:
        if not some_num % num:
            prime_list.append(num)
    return True if not prime_list else False



