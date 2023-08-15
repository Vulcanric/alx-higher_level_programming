#!/usr/bin/python3

def fizzbuzz():
    """Prints the number from 1 to 100 seperated by a space

    For multiples of three, it prints 'Fizz' instead of the number
    For multiples of five, it prints 'Buzz' instead of the number
    For multiples of both three and five, prints 'FizzBuzz'
    """
    for i in range(1, 101):
        if i % 15 == 0:  # When i is both multiple of 3 and 5
            print('FizzBuzz', end=' ')
        elif i % 3 == 0:  # When i is multiple of 3 alone
            print('Fizz', end=' ')
        elif i % 5 == 0:  # When i is multiple of 5 alone
            print('Buzz', end=' ')
        else:  # Otherwise, print number as is
            print(i, end=' ')
