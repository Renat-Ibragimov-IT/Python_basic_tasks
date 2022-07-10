# Write a function that will remove elements with empty values from dict:
# {'1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': None}
# Should return {'1': 'One', '2': 'Two', '3': 'Three', '4': 'Four'}

initial_dict = {'1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': None}


def clear_dict(some_dict: dict) -> dict:
    """This function will remove the empty values from the dict"""
    return {key: value for key, value in some_dict.items() if value}


print(clear_dict(initial_dict))
