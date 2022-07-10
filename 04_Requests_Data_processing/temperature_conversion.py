# Write a temperature calculator.
# The user enters the number and type of temperature
# (C, F, K - Celsius, Fahrenheit, Kelvin respectively)
# The program should display the temperature in three temperature scales -
# Celsius, Fahrenheit, Kelvin.

user_temp = float(input('Please enter degree to convert: '))
initial_temp = input('Please enter initial temperature type "C" for Celsius, '
                     '"F" for Fahrenheit or "K" for Kelvin: ')
final_temp = input('Please enter final temperature type "C" for Celsius, '
                   '"F" for Fahrenheit or "K" for Kelvin: ')


def temperature_converter(deg: float, initial: str, final: str) -> float:
    """This function will take the temperature and its types as arguments
    and return result of conversion"""
    formulas = {'CF': deg * 1.8 + 32, 'CK': deg + 273.15,
                'FC': ((deg - 32) * 5) / 9, 'FK': ((deg + 459.67) * 5) / 9,
                'KC': deg - 273.15, 'KF': 1.8 * (deg - 273.15) + 32}
    dict_key = initial + final
    return round(formulas[dict_key], 2)


print(f'Result is: '
      f'{temperature_converter(user_temp, initial_temp, final_temp)}')
