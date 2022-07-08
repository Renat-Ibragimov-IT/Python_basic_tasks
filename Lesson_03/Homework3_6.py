# 6. Шахматный конь ходит буквой “Г” — на две клетки по вертикали в любом
# направлении и на одну клетку по горизонтали, или наоборот.
# Даны две различные клетки шахматной доски, определите,
# может ли конь попасть с первой клетки на вторую одним ходом.

horizontally = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
vertically = ['1', '2', '3', '4', '5', '6', '7', '8']

initial_square = str(input("Please enter initial knight square: "))
in_sq = str.lower(initial_square)
ind_letter1 = int(horizontally.index(in_sq[0]))
ind_digit1 = int(vertically.index(in_sq[1]))

next_square = str(input("Please enter next knight square to check: "))
next_sq = str.lower(next_square)
ind_letter2 = int(horizontally.index(next_sq[0]))
ind_digit2 = int(vertically.index(next_sq[1]))

if abs(ind_letter1 - ind_letter2) == 2 and abs(ind_digit1 - ind_digit2) == 1 \
 or abs(ind_letter1 - ind_letter2) == 1 and abs(ind_digit1 - ind_digit2) == 2:
    print("Yes! It is the right move!")
else:
    print("No! It is not the right move!")

