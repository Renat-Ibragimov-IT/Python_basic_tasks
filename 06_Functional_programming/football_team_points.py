# 1. Write a function that will count the number of points
# of the football team.
# A win is 3 points, a draw is 1 point, a loss is 0 points.
# The function takes three arguments - win, draw, loss.
# Example : count_points(3, 2, 2) -> 11


def football_count(win: int, draw: int, loss: int) -> int:
    """This function will return total count points depending on the number of
       wins, draws and losses"""
    return win * 3 + draw + (loss * 0)


print(football_count(3, 2, 2))
