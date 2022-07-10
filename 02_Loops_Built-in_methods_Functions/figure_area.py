# Write a program that will return the area of the figure:
# by default a triangle, optionally a square.


def figure_selection() -> str:
    """This function will receive the user's input and return figure name
    if the user entered a figure from the list of available figures"""
    choices = ('triangle', 'square')
    while True:
        user_input = input("Please enter figure (triangle or square): ")
        if user_input not in choices:
            print('Incorrect figure input')
            continue
        return user_input


def figure_area(user_figure: str) -> float:
    """This function will receive the figures name and calculate area of the
    given figure"""
    if user_figure == 'triangle':
        side_a = float(input("Please enter length of triangular side (a): "))
        side_b = float(input("Please enter length of triangular side (b): "))
        side_c = float(input("Please enter length of triangular side (c): "))
        p = (side_a + side_b + side_c) * 0.5  # semi-perimeter
        return round((p * (p - side_a) * (p - side_b) * (p - side_c))
                     ** 0.5, 1)  # Heron's formula
    sq_side = float(input("Please enter length of square side: "))
    return round(sq_side ** 2, 1)


print("Your figure area is", figure_area(figure_selection()), "cm")
