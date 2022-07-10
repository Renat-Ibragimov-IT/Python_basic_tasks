# Given a list of values. Return a dictionary where each key is the index of
# the list and the value of the list is the value of the key:
# Input:
# ['a', 'b', 'c', 'd', 'e']
# Output:
# {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e'}

user_list = ['a', 'b', 'c', 'd', 'e']


def list_indexing(some_list: list) -> dict:
    """This function will receive some list and return dict"""
    return dict(enumerate(some_list))


print(list_indexing(user_list))
