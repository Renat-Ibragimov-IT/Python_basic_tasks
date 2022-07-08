# 1. On the first day, the athlete ran `x` kilometers, and then every day he
# increased the distance by 10% from the previous value. Given the number `y`,
# determine the number of the day on which the athlete will run at least `y`
# kilometers. The program receives the numbers `x` and `y` as input and must
# output one number - the number of the days.
initial_dist = float(input("Please enter initial distance: "))
target_dist = float(input("Please enter target distance: "))


def target_dist_calc(initial_distance: float, target_distance: float) -> str:
    """This function calculates how many days the athlete will need to achieve
    the intended goal. The function arguments are two numbers received from the
    user: the distance that the athlete covered on the first day and the
    distance to which he aspires"""
    days = 1
    mileage = initial_distance
    while mileage < target_distance:
        mileage *= 1.1
        days += 1
    return f'To achieve the target distance You have to train {days} days'


print(target_dist_calc(initial_dist, target_dist))
