# 1. Написать функцию которая посчитает количество очков футбольной команды.
# Победа дает 3 очка, ничья 1 очко, поражение 0 очков.
# Функция принимает три аргумента - win, draw, loss.
# Пример : count_points(3, 2, 2) -> 11


def football_count(win: int, draw: int, loss: int) -> int:
    """This function will return total count points depending on the number of
       wins, draws and losses"""
    return win * 3 + draw


print(football_count(3, 2, 2))
