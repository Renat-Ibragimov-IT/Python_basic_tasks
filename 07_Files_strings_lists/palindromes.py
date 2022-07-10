# Write a function that will determine if the input string is a palindrome
# (one that reads the same on either side)
# For example: 12321, ABBA, Hannah, level

user_sentence = 'Mr. Owl ate my metal worm!'


def palindrome(string: str) -> str:
    """This function checks if the given word is a palindrome"""
    sentence_to_check = "".join(symbol for symbol in string if
                                symbol.isalnum()).lower()
    return 'Palindrome' if sentence_to_check == sentence_to_check[::-1] \
        else 'Not Palindrome'


print(f'{"Your sentence is: "}{palindrome(user_sentence)}')

