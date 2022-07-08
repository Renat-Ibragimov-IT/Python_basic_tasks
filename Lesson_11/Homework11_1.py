# 1. Программа которая при запуске должна:
# Создать текстовый файл, записать в него построчно данные, которые вводит
# пользователь. Окончанием ввода пусть служит пустая строка. Каждая введённая
# строка, в файле, должна начинаться с новой строки.

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
