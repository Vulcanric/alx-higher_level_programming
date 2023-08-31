#!/usr/bin/python3

from random import randint
while True:
    number = randint(1, 10)
    guess = float(input("Guess the number: "))

    try:
        if guess == number:
            break
        else:
            print("Oops! Try again")
    except ValueError:
        print("Please enter a valid number!")
    except Exception as ex:
        print("An unknown error happened:", ex)

print("You guessed it!")
