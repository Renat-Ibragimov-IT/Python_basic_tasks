# Given a natural number. It is required to determine whether the year with the
# given number is a leap year. If the year is a leap year, then print `YES`,
# otherwise print `NO`. Recall that in accordance with the Gregorian calendar,
# a year is a leap year if its number is a multiple of 4 but not a multiple of
# 100, and also if it is a multiple of 400.

while True:
    while True:
        year = int(input('If you want to check if a year is a leap year, just '
                         'enter the year here!: '))
        print("Leap year") if (year % 4 == 0 and year % 100 != 0) \
                              or year % 400 == 0 else print("Not a Leap year")
        repeat = str(input('Do You want to check another year? '
                           'Enter "Yes" or "No": '))
        if repeat == 'No' or repeat == 'no' or repeat == 'n' or repeat == "NO":
            print("Thank You! Good by!")
            import sys
            sys.exit()
        elif repeat == 'Yes' or repeat == "yes" or repeat == "y" \
                or repeat == "YES":
            continue
        else:
            print('Please enter only "Yes" or "No"!')
            break
