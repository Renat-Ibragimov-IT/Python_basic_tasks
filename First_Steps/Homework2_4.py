# 4. Дано натуральное число. Требуется определить, является ли год с данным
# номером високосным. Если год является високосным, то выведите `YES`,
# иначе выведите `NO`. Напомним, что в соответствии с григорианским календарем,
# год является високосным, если его номер кратен 4, но не кратен 100, а также
# если он кратен 400.

print("Hi, dude!")
while True:
    while True:
        year = int(input('If you want to check if a year is a leap year, just enter '
                  'the year here!: '))

        cond01 = year % 4 == 0
        cond02 = year % 100 == 0
        cond03 = year % 400 == 0

        if cond01 is False: print\
            ("\033[1m\033[31m{}\033[0m".format("This year is not a leap year"))
        if cond01 is True and cond02 is False: print("\033[1m\033[32m{}\033[0m"
                                    .format("This year is a leap year"))
        if cond01 is True and cond02 is True and cond03 is False: print\
            ("\033[1m\033[31m{}\033[0m".format("This year is not a leap year"))
        if cond01 is True and cond02 is True and cond03 is True: print\
            ("\033[1m\033[32m{}\033[0m".format("This year is a leap year"))
        else: break
    repeat = str(input('Do You want to check another year? '
                       'Enter "Yes" or "No": '))
    if repeat == 'No' or repeat == 'no' or repeat == 'n' or repeat == "NO":
        print("Thank You! Good by!")
        import sys
        sys.exit()
    elif repeat == 'Yes' or repeat == "yes" or repeat == "y" or repeat == "YES":
        continue

# Ну или так:/

year = int(input('Enter the year here!: '))
if year % 100 == 0: print("Not a Leap year")
elif year % 4 == 0 or year % 400 == 0: print("Leap year")
else: print("Not a Leap year")

# Или вот так, ваще круто

n = int(input('Enter year:'))
print('leap') if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0 else print('not leap')


