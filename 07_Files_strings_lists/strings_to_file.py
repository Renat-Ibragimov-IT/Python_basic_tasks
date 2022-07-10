# A program that, when run, should:
# Create a text file, write to it line by line the data that the user enters.
# Let the input end with an empty string. Each line entered in the file should
# start on a new line.

user_string_list = []
while (string := input("Enter sentence: ")) != '':
    user_string_list.append(string)


def new_file(user_list: list):
    """This function will create a new txt file and write inside all user's
    strings with the new line"""
    with open('user-string-list.txt', 'a') as file:
        for element in user_list:
            file.write(element)
            file.write('\n')


new_file(user_string_list)
