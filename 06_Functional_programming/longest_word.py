# 3. Написать функцию которая вернет самое длинное слово в строке:
# longest_word("What makes a good man") -> makes

user_string = input("Please enter some sentence: ")
# Variant 1


def longest_word(sentence: str) -> str:
    """This function will return the longest word in sentence
                                                         (non-cheat method)"""
    split_string = sentence.split()
    index = len(split_string) - 1
    long_word = split_string[-1]
    while index:
        if len(long_word) < len(split_string[index-1]):
            long_word = split_string[index-1]
        index -= 1
    return long_word


print("Longest word in sentence is: ", longest_word(user_string))

# Variant 2


def longest_word_1(sentence: str) -> str:
    """This function will return the longest word in sentence (cheat method)"""
    return max(sentence.split(), key=len)


print("Longest word in sentence is: ", longest_word_1(user_string))
