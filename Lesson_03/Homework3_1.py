# 1. Пользователь вводит трехзначное число. Найдите сумму его цифр.

# Variant #1

any_integer_number = input("Please enter any integer number: ")
result = sum(int(digit) for digit in any_integer_number)
print("Sum of digits in Your number is: ", result)

# Variant #2

number = int(input("Please enter any integer number: "))
sum = 0
while number > 0:
    digit = number % 10
    sum = sum + digit
    number = number // 10
print("Sum of digits in Your number is: ", sum)

# Variant 3

print(sum([int(num) for num in input("Please enter number: ")]))
