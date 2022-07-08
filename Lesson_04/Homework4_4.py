# 4. По данному натуральному `n ≤ 9` выведите лесенку из `n` ступенек,
# `i`-я ступенька состоит из чисел от 1 до `i` без пробелов.
#    1
#    12
#    123
#    1234
#    12345

user_number = int(input("Please enter any digit from 1 to 9: "))


def stairs_creating():
    str_for_print = ''
    for digit in range(1, (user_number + 1)):
        str_for_print = str_for_print + str(digit)
        print(str_for_print)


stairs_creating()
