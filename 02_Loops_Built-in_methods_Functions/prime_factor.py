# Write a function `is_prime` that takes 1 argument - number and returns
# `True` if prime, `False` otherwise.

def user_number() -> int:
    """This function will get, check and return the number if it matches the
    conditions"""
    number = int(input("Please enter number from 1 to 1000 to check if it is "
                       "a prime number: "))
    if 0 <= number <= 1000:
        return number
    else:
        print("Incorrect number")
    return user_number()


def is_prime(number_to_check: int) -> int:
    """This function will check if a number is prime"""
    final_number = 2
    while number_to_check % final_number:
        final_number += 1
    return True if final_number == number_to_check else False


print(is_prime(user_number()))
