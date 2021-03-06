# The user enters a number from 1 to 10, the program generates a random number
# from 1 to 10, if the numbers are equal print 'You won!' if not - 'You lose!'.
# Give the user three tries.
import random

random_number = random.randint(1, 10)
attempt = 0
while attempt < 3:
    user_number = int(input("Please enter number from 1 to 10: "))
    attempt += 1
    if user_number == random_number:
        print("You won!")
        break
    attempt_vars = {1: "Please try again! You have two attempts!",
                    2: "Please try again! You have last attempt!",
                    3: "You lose! GAME OVER"}
    print(attempt_vars[attempt])
