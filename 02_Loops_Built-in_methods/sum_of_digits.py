# The user enters a three-digit number. Find the sum of its digits.

# Variant #1

any_integer_number = input("Please enter any integer number: ")
result = sum(int(digit) for digit in any_integer_number)
print(f'Sum of digits in Your number is: {result}')

# Variant #2

number = int(input("Please enter any integer number: "))
amount = 0
while number > 0:
    digit = number % 10
    amount = amount + digit
    number = number // 10
print(f'Sum of digits in Your number is: {amount}')
