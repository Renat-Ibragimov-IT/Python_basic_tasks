# 4. Given a natural number `n ≤ 9`, print a stairs with `n` steps,
# The `i`-th step consists of numbers from 1 to `i` without spaces.
#    1
#    12
#    123
#    1234
#    12345
def user_number() -> int:
    """This function will return the number entered by user"""
    number_of_stairs = int(input("Please enter any digit from 1 to 9: "))
    return number_of_stairs


def stairs_creating(number: int) -> str:
    """This function will create the "stairs" of numbers with the amount of
    steps depending on the number passed in the argument"""
    steps = []
    str_for_print = ''
    for digit in range(1, (number + 1)):
        str_for_print = str_for_print + str(digit)
        steps.append(str_for_print)
    return '\n'.join(steps)


print(stairs_creating(user_number()))
