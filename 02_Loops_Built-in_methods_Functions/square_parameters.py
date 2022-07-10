# Write a function "square" that takes 1 argument, the side of the square,
# and returns 3 values (using a tuple): the perimeter of the square,
# the area of the square and the diagonal of the square.

def square(square_side: float) -> tuple:
    """This function will receive the side of the square and return
    the perimeter of the square, the area of the square
    and the diagonal of the square."""
    return square_side * 4, square_side ** 2, \
           round(square_side * (2 ** 0.5), 1)


print(f'The perimeter of the square is: {square(5.5)[0]}')
print(f'The area of the square is: {square(5.5)[1]}')
print(f'The diagonal of the square is: {square(5.5)[2]}')
