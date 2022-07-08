# 1. Написать функцию которая вернет строку введенную пользователем.
# Обернуть функцию в декоратор чтобы функция вместо строки целиком вернула
# список слов.

def sentence_to_words(func):

    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).split()
    return wrapper


@sentence_to_words
def user_sentence() -> str:
    return input('Please enter any sentence: ')


print(user_sentence())
