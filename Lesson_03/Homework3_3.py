# 3. Напечатать список list_ten = [10, 20, 30, 40, 50] реверсивно т.е.
# программа должна вернуть [50, 40, 30, 20, 10].

# Variant 1

list_ten = list(range(10, 51, 10))
list_ten.reverse()
print(list_ten)

# Variant 2

list_ten2 = list(range(10, 51, 10))
rev_list = list_ten2[::-1]
print(rev_list)
