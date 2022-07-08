# 4. Дан список случайных целых чисел. Замените все нечетные числа списка
# нулями. И выведете их количество.

import random
user_list = []
amount_of_numbers_in_the_list = 10
while amount_of_numbers_in_the_list > 0:
    user_list.append(random.randrange(1, 1000))
    amount_of_numbers_in_the_list -= 1


def new_list():
    replace_list = []
    for num in user_list:
        if num % 2 == 0:
            replace_list.append(num)
        else:
            replace_list.append(num * 0)
    corrected_list = list(num for num in replace_list if num == 0)
    return user_list, replace_list, len(corrected_list)


print("Random numbers list:", new_list()[0])
print("List with replaced odd number:", new_list()[1])
print("Amount of odd numbers:", new_list()[2])
