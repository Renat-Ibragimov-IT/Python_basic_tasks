# 2. Написать калькулятор температур.
# Пользователь вводит число и тип температуры (C, F, K - Цельсий, Фарренгейт,
# Кельвин соответственно)
# Программа должна вывести температуру в трех шкалах температур - Цельсий,
# Фарренгейт, Кельвин.

user_temp = float(input('Please enter degree to convert: '))
initial_temp = input('Please enter initial temperature type "C" for Celsius, '
                     '"F" for Fahrenheit or "K" for Kelvin: ')
final_temp = input('Please enter final temperature type "C" for Celsius, '
                   '"F" for Fahrenheit or "K" for Kelvin: ')

# Variant 1


def celsius(temp_deg: float, temp_type: str) -> float:
    return temp_deg * 1.8 + 32 if temp_type == 'F' \
        else temp_deg + 273.15


def fahrenheit(temp_deg: float, temp_type: str) -> float:
    return ((temp_deg - 32) * 5) / 9 if temp_type == 'C' \
        else ((temp_deg + 459.67) * 5) / 9


def kelvin(temp_deg: float, temp_type: str) -> float:
    return temp_deg - 273.15 if temp_type == 'C' \
        else 1.8 * (temp_deg - 273.15) + 32


def choice(user_choice: str) -> float:
    if initial_temp == 'C':
        print("Result is: ", celsius(user_temp, final_temp))
    if initial_temp == 'F':
        print("Result is: ", fahrenheit(user_temp, final_temp))
    if initial_temp == 'K':
        print("Result is: ", kelvin(user_temp, final_temp))


choice(initial_temp)

# Variant 2


def converter(temp: float, in_type: str, fin_type: str):
    if in_type == 'C':
        return temp * 1.8 + 32 if fin_type == 'F' \
            else temp + 273.15
    if in_type == 'F':
        return ((temp - 32) * 5) / 9 if fin_type == 'C' \
            else ((temp + 459.67) * 5) / 9
    if in_type == 'K':
        return temp - 273.15 if fin_type == 'C' \
            else 1.8 * (temp - 273.15) + 32


print('Result is: ', round(converter(user_temp, initial_temp, final_temp), 2))

# Variant 3


def temp_conv(deg: float, initial: str, final: str):
    formulas = {'CF': deg * 1.8 + 32, 'CK': deg + 273.15,
                'FC': ((deg - 32) * 5) / 9, 'FK': ((deg + 459.67) * 5) / 9,
                'KC': deg - 273.15, 'KF': 1.8 * (deg - 273.15) + 32}
    dict_key = initial + final
    return print('Result is: ', round(formulas[dict_key], 2))


temp_conv(user_temp, initial_temp, final_temp)
