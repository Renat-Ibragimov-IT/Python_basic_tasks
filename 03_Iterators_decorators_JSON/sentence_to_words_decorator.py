# Write a function that will return the string entered by the user.
# Wrap the function in a decorator so that the function returns
# a list of words instead of a string.

def sentence_to_words(func):
    """This decorator will split the sentence to the words"""
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).split()
    return wrapper


@sentence_to_words
def user_sentence() -> str:
    """This function will return the user's sentence"""
    return input('Please enter any sentence: ')


print(user_sentence())
