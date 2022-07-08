# 3. Даны два целых числа `A` и `В`. Выведите все числа от `A` до `B`
# включительно, в порядке возрастания, если `A < B`, или в порядке убывания
# в противном случае.


def range_creation():
    number1 = int(input("Please enter the fist number: "))
    number2 = int(input("Please enter the second number: "))
    if number1 < number2:
        print(list(range(number1, (number2 + 1))))
    elif number1 > number2:
        print(list(range(number1, (number2 - 1), -1)))


range_creation()

# or


def range_creation1(num1, num2):
    if num1 < num2:
        print(list(range(num1, (num2 + 1))))
    elif num1 > num1:
        print(list(range(num1, (num2 - 1), -1)))


range_creation1(20, 42)
