# The user enters the number "x", which has two digits after the decimal point.
# - Print its fractional part.
# - Print its first digit after the decimal point.

float_num = input("Please enter float number (in format x.xx): ")
split_number = float_num.split('.')
print(f'An integer: {split_number[0]}')
print(f'First digit after the dot: {split_number[1][0]}')


