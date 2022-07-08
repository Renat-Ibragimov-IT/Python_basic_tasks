# 2. Написать функцию которая определит является ли введенная строка
# палиндромом (та которая читается одинаково с любой стороны), пример:
# ШАЛАШ, КАЗАК, ДЕД, ДОХОД, 13231 и т.д.

user_sentence = 'Mr. Owl ate my metal worm!'


def palindrome(string: str) -> str:
    """This function checks if the given word is a palindrome"""
    sentence_to_check = "".join(symbol for symbol in string if
                                symbol.isalnum()).lower()
    return 'Palindrome' if sentence_to_check == sentence_to_check[::-1] \
        else 'Not Palindrome'


print(f'{"Your sentence is: "}{palindrome(user_sentence)}')


