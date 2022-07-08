# 3. Написать функцию которая вернет площадь фигуры: по-умолчанию треугольника,
# опционально квадрата. На входе 2 величины и параметр типа фигуры.
# user_figure = int(input('Please enter "1" for triangular or "2" for square: '))


def figure_area(user_figure: int):

    if user_figure == 1:
        side_a = float(input("Please enter length of triangular side (a): "))
        side_b = float(input("Please enter length of triangular side (b): "))
        side_c = float(input("Please enter length of triangular side (c): "))
        p = (side_a + side_b + side_c) * 0.5  # semi-perimeter
        return round((p * (p - side_a) * (p - side_b) * (p - side_c))
                     ** 0.5, 1)  # Heron's formula
    if user_figure == 2:
        sq_side = float(input("Please enter length of square side: "))
        return round(sq_side ** 2, 1)
    else:
        return figure_area(int(input('Please enter only "1" or "2": ')))


# print("Your figure area is", figure_area(user_figure), "cm")
def figure() -> int:
    choices = {'triangle': 1, 'square': 0}
    while True:
        user_input = input("Please enter figure (triangular or square): ")
        choice = choices.get(user_input)
        if choice is None:
            print('Incorrect figure input')
            continue
        return choice


def small_figure_area(figure, side_a: int, side_b: int):
    return side_a * side_b * 0.5 if figure() == 1 else side_a * 4


print(small_figure_area(figure, 10, 10))
