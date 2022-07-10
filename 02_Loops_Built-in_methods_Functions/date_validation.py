# Write a function `is_date` that takes 3 arguments - day, month and year.
# Return `True` if the date is valid
# (the day of the month must be taken into account.
# For example, 30.02 is not a valid date, also 31.06 or 32.07, etc.)
# and `False` otherwise.
import datetime
user_day = int(input("Please enter day of the month: "))
user_month = int(input("Please enter month: "))
user_year = int(input("Please enter year: "))


def is_date(day: int, month: int, year: int):
    """This function will check if the date entered is correct."""
    try:
        datetime.datetime(day=day, month=month, year=year)
        return True
    except ValueError:
        return False


print(f'Entered date is: {is_date(user_day, user_month, user_year)}')
