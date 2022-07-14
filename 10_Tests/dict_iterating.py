# Given two tuples, write a function that will combine them into one dict:
#   Input:
#   integers = (1, 2, 3, 4)
#   strings = ('one', 'two', 'three', 'four')
#   Output:
#   {1: 'one', 2: 'two', 3: 'three', 4: 'four'}

integers = (1, 2, 3, 4)
strings = ('one', 'two', 'three', 'four')


def merging_into_dict(some_tuple: tuple, some_tuple_2: tuple) -> dict:
    """This function will receive two tuples and combine in into one dict"""
    return dict(zip(some_tuple, some_tuple_2))


print(merging_into_dict(integers, strings))
