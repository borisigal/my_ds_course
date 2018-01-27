# import necessary module

import random

# The computer "chooses" a number

my_number = random.randint(1, 100)

# The program asks you to play

print("I have chosen a number between 1 and 100.")

print("Please try to guess it...")

# The program reads your guess and stores it



user_guess = int(input())

# The game is on...



high_wrong="You are too high, please try again..."

low_wrong="You are too low, please try again..."



while my_number != user_guess:

    print(high_wrong) if user_guess > my_number else print(low_wrong)

    user_guess = int(input())

       

print("Finally :-)\nGAME OVER")







"""

triple quotes

are used for block remarks



"""