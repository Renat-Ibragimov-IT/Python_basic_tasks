1. Напишите программу, которая приветствует пользователя, выводя слово
`Hello`, введенное имя и знаки препинания по образцу: Hello, Kitty!

meeting  = input("What's your name?: ")
print("\033[1m\033[3m\033[33m{}\033[0m".format('Hello, my dear ' + meeting +
'! ') + "\033[1m\033[3m\033[34m{}\033[0m".format('I have always dreamed '
                                        'of meeting you! ' + 'Honestly!'))

offer = print("Let's start? (Yes or No): ")
while True:
    answer = str(input())
    if answer == 'Yes' or answer == "yes" or answer == "y" or answer == "YES":
        print("\033[1m\033[32m{}\033[0m".format(
        "Wow! Brilliant! I'm happy!" + '(o˘◡˘o)'))
        break
    elif answer == 'No' or answer == 'no' or answer == 'n' or answer == "NO":
        print("\033[1m\033[30m{}\033[0m".format('Okay! Next time!' +
                                                '¯\_(ツ)_/¯'))
        break
    else:
        print("\033[1m\033[3m\033[31m{}\033[0m".format
        ('No,no,no! Give me a specific answer! Only "Yes" or "No"' +
         '(º _ º)'))
        continue

print("О така хуйня, малята...")

username = input("What is Your name?: ")
print("Hello, " + username + "!")
