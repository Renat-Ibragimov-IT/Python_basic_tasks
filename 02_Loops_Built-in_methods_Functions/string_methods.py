# Write a program that will return the number of words entered by the user and
# the total number of characters.
def user_input() -> str:
    """This function will receive and return user's sentence"""
    user_sentence = input("Please enter any sentence: ")
    return user_sentence


some_sentence = user_input()


def amount_of_symbols(sentence: str) -> int:
    """This function will calculate amount of symbols in given sentence"""
    return len(sentence.replace(" ", ""))


def amount_of_words(sentence: str) -> int:
    """This function will calculate amount of words in given sentence"""
    return len(sentence.split())


print(f'Amount of symbols in sentence: '
      f'{amount_of_symbols(some_sentence)}')
print(f'Amount of words in sentence: '
      f'{amount_of_words(some_sentence)}')
