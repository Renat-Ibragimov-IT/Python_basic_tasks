# Given a string.
# a. print the third character of this string.
# b. print the penultimate character of this string.
# c. print the first five characters of this string.
# d. print the entire string except for the last two characters.
# e. print all characters with even indices (assuming that indexing starts from
#    0, so the characters are printed starting from the first).
# f. print all characters with odd indices, i.e. starting from the second
#    character of the string.
# g. output all characters in reverse order.
# h. print all characters of the string one by one in reverse order, starting
#    with the last one.
# i. print the length of the given string.

some_str = 'hkd3145m131kfhgd^46*@F6h4s!@$5%fgfsvs@%$@'

print("a.", some_str[2])
print("b.", some_str[-2])
print("c.", some_str[:5])
print("d.", some_str[:-2])
print("e.", some_str[::2])
print("f.", some_str[1::2])
print("g.", some_str[::-1])
print("h.", some_str[::-2])
print("i.", len(some_str))
