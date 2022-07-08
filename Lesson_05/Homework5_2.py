# 2. Написать программу которая вернет количество введенных пользователем слов
# и общее число символов.

user_str = input("Please enter any sentence: ")


def amount_of_symbols_and_words():
    return len(user_str.replace(" ", "")), len(user_str.split())


print("Amount of symbols in sentence: ", amount_of_symbols_and_words()[0])
print("Amount of words in sentence: ", amount_of_symbols_and_words()[1])
