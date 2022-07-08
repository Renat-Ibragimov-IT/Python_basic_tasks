# Given a list:
# list_of_six = [100, 106, 112, 118, 124, 130, 136, 142, 148, 154, 160, 166,
# 172, 178, 184, 190, 196]
# Print all numbers that are divisible by 5 without a remainder,
# but not more than 150.

list_of_six = [100, 106, 112, 118, 124, 130, 136, 142, 148, 154, 160, 166,
               172, 178, 184, 190, 196]
print([num for num in list_of_six if num % 5 == 0 and num <= 150])
