# Write a program that will find the factorial of the number
# entered by the user.
# For example, the factorial of 5 is 1 * 2 * 3 * 4 * 5 = 120.
# Factorial formula:
# n! = 1 * 2 * ... * n, where 'n' is the number entered by the user.

user_number = int(input("Please enter some number: "))
number = int(user_number)
result = 1
while number >= 1:
    result = result * number
    number = number - 1
print(f'Factorial of number {user_number} is {result}')
