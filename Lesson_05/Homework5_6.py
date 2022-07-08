# 6. Написать функцию которая уберет из dict элементы с пустыми значениями:
#    {'first_color': 'Red', 'second_color': 'Green', 'third_color': None}
#    Должно вернуть {'first_color': 'Red', 'second_color': 'Green'}
#    * dict может быть произвольным

some_dict = {'1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': None}


def clear_dict(x: dict):
    return {key: value for key, value in some_dict.items() if value}


print(clear_dict(some_dict))
