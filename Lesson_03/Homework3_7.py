#7. Написать программу которая найдет факториал введенного пользователем числа.
# Например, факториал числа 5 равен произведению 1 * 2 * 3 * 4 * 5 = 120.
# Формула нахождения факториала:
# n! = 1 * 2 * … * n, где n - введенное пользователем число.

user_number = input("Please enter some number: ")
number = int(user_number)
result = 1
while number >= 1:
    result = result * number
    number = number - 1
print("Factorial of number", user_number, "is", result)
