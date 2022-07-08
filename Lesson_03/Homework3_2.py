# 2. Пользователь вводит действительное (вещественное) число `X`, которое имеет
# два знака после десятичной точки.
# - Выведите его дробную часть.
# - Выведите его первую цифру после десятичной точки.

float_num = input("Please enter float number (in format x.xx): ")
split_number = float_num.split('.')
print("An integer: ", split_number[0])
print("First digit after the dot: ", split_number[1][0])


