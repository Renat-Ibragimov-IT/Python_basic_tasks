# The program receives the number x as input.
# Given a list of 10 items [10, 20, 30, 40, 50, 60, 70, 80, 90, 100].
# Write a program that will return:
# - Whether x is present among the elements.
# - The input number can be either an integer, float, or negative.
# - i.e. x = -10.00 should return that x is in the list.
# ** Ideally, the list should be written as a tuple, once.

digits = tuple(range(10, 101, 10))
num = float(input('Enter Your number number here: '))
num_module = round(abs(num))
if num_module in digits:
    print("The number is in the tuple")
else:
    print("The number is not in the tuple")

