# Write a function that will replace a word in the text with another one.
# The function takes 4 arguments, the original string, the word to be replaced,
# the new word, the number of replacements, example:
# fake_string('DC makes good movies, DC makes good comics', 'DC', 'Marvel', 1)
# -> 'Marvel makes good movies, DC makes good comics'
# fake_string('DC makes good movies, DC makes good comics', 'DC', 'Marvel', 2)
# -> 'Marvel makes good movies, Marvel makes good comics'

user_sentence = 'DC makes good movies, DC makes good comics'


def replace_words(sentence: str, change_from: str, change_to: str, qty: int):
    """This function will return the user sentence with replaced words
                                                depending on user's request"""
    return sentence.replace(change_from, change_to, qty)


print(replace_words(user_sentence, 'DC', 'Marvel', 2))

# I don't do many inputs to keep it simple. But we can use user input for
# "change_from"-word, "change_to"-word and quantity of changes.
# Also, we can use arguments if needed.
