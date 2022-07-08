# 3. Two integers `A` and `B` are given. Print all numbers from `A` to `B`
# inclusive. In ascending order if `A < B`, or in descending order otherwise.
def user_input() -> tuple:
    """This function will return the tuple of numbers entered by user"""
    number1 = int(input("Please enter the fist number: "))
    number2 = int(input("Please enter the second number: "))
    return number1, number2


def range_creation(numbers: tuple) -> list:
    """This function will create the range between two numbers received as
    arguments"""
    return list(range(numbers[0], (numbers[1] + 1))) \
        if numbers[0] < numbers[1] \
        else list(range(numbers[0], (numbers[1] - 1), -1))


print(range_creation(user_input()))
