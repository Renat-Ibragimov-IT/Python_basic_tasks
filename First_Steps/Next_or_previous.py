# Write a program that reads an integer and outputs text similar to the one in
# the example (spaces are important!). The first line contains the next value,
# and the second line contains the previous value of the entered number:
# Please enter an integer number: 258
# The next number for the number 258 is 259.
# The previous number for the number 258 is 257.
#     or
# Please enter an integer number: 0
# The next number for the number 0 is 1.
# The previous number for the number 0 is -1.

initial_int = int(input('Please enter an integer number: '))
print(f'The next number for the number {initial_int} is {initial_int+1}')
print(f'The previous number for the number {initial_int} is {initial_int-1}')
