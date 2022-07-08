# 5. Написать функцию square, принимающую 1 аргумент — сторону квадрата,
# и возвращающую 3 значения (с помощью кортежа): периметр квадрата,
#   площадь квадрата и диагональ квадрата.

def square(square_side: float):
    return square_side * 4, square_side ** 2, \
           round(square_side * (2 ** 0.5), 1)


print(square(6.3))
