# 3. Дан список значений. Вернуть словарь где каждый ключ - это индекс списка,
# а значение списка - это значение ключа:
# Input:
# ['a', 'b', 'c', 'd', 'e']
# Output:
# {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e'}

user_list = ['0', '1', '2', '3', '4', '5']


def list_indexing(some_list: list) -> dict:
    return dict(enumerate(some_list))


print(list_indexing(user_list))
