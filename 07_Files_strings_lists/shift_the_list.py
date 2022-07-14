# Write a function that will shift the resulting list by N elements to the
# right or left, the accepted arguments are a list and a natural number
# (if negative, shift to the left, positive - to the right).

user_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def shift_list(some_list: list, shift_by: int):
    """This function will return shifted user list with step given by user"""
    count = abs(shift_by)
    while count > 0:
        if shift_by > 0:
            some_list = some_list[-1:] + some_list[:-1]
        else:
            some_list = some_list[1:] + some_list[:1]
        count -= 1
    return some_list


print(shift_list(user_list, 4))
