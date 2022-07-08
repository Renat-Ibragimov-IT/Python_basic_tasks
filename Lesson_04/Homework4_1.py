# 1. В первый день спортсмен пробежал `x` километров, а затем он каждый день
# увеличивал пробег на 10% от предыдущего значения. По данному числу `y`
# определите номер дня, на который пробег спортсмена составит не менее `y`
# километров. Программа получает на вход числа `x` и `y` и должна вывести одно
# число - номер дня.


def target_dist_calc():
    initial_dist = float(input("Please enter initial distance: "))
    target_dist = float(input("Please enter target distance: "))
    days = 1
    while initial_dist < target_dist:
        initial_dist *= 1.1
        days += 1
    print("To achieve the target distance You have to train", days,
          "days")


target_dist_calc()
