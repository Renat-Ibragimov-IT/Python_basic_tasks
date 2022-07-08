# 3. Длина маршрута велоралли "100 километров за 10 часов по Поясу Славы" -
# примерно 100 километров. Велосипедист Вася стартует с нулевого километра
# маршрута и едет со скоростью `v` километров в час. На какой отметке он
# остановится через `t` часов? Программа получает на вход значение `v` и `t`.
# Если `v > 0`, то Вася движется в положительном направлении по маршруту,
# если же значение `v < 0`, то в отрицательном. Программа должна вывести целое
# число от 0 до 100 — номер отметки, на которой остановится Вася.

start = print('Hi, Vasya! Are You ready to start "100 km along the Belt of '
              'Glory" bicycle rally? (Yes or No): ')
while True:
    answer = str(input())
    if answer == 'No' or answer == 'no' or answer == 'n' or answer == 'NO':
        print("\033[1m\033[3m\033[31m{}\033[0m".format("RUSSIAN WARSHIP IDI "
                                                       "NAHUY!!!"))
        import sys
        sys.exit()
    elif answer == 'Yes' or answer == 'yes' or answer == 'y' or answer == \
            'YES':
        question = print('Great! Tell me your maximum speed km/hr: ')
        break
    else: print('Please input only "Yes" or "No": ')

while True:
    try:
        speed = int(input())
    except: print("Please input only integer number: ")
    else: break
if speed <= 0:
    import sys
    sys.exit('LOOKS LIKE YOU GOT LOST, RUSSIAN ORK! UKRAINIAN ARMY ARE '
             'LOOKING FOR YOU ALREADY!!!')
elif speed > 0:
    question01 = print("Very well! You'r so fast! How many hours can you "
                           "drive?: ")

while True:
    try:
        while True:
            time = int(input())
            if time <= 0: print("Please input only positive integer number: ")
            else: break
    except: (TypoError): print("Please input only positive "
                                           "integer number: ")
    else: break

dist = speed*time

if dist <= 100:
    print('You were only able to cover', "\033[1m\033[3m\033[31m{}\033[0m"
    .format(dist) , 'km before Bayraktar killed You!\n',"\033[1m\033[3m\033"
    "[31m{}\033[0m".format("YOU'RE DEAD ALREADY, RUSSIAN SWINEDOG!!!"))

    import sys
    sys.exit()
elif dist > 100:
    print("Hmmm! You covered", "\033[1m\033[3m\033[31m{}\033[0m".format(dist),
    "km and overtook your platoon.""\n", "\033[1m\033[3m\033[31m{}\033[0m"
    .format("That's why you became an easy target for a sniper!"), "\n",
    "\033[1m\033[3m\033[31m{}\033[0m".format("WELCOME TO HELL, BASTARD!!!"))
    import sys

    sys.exit()

