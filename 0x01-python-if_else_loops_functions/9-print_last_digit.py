#!/usr/bin/python3

def print_last_digit(number):
    """Function prints the last digit of a number
    """
    last_digit = 0  # declaring a variable to hold the value of the last digit

    if number >= 0:  # If the number is positive
        # get the last digit (the remainder of number's division by 10)
        last_digit = number % 10
    else:  # Otherwise let it be the remainder of number's division by -ve 10
        last_digit = number % -10

    # Getting the absolute value of last digit
    last_digit = abs(last_digit)

    print(last_digit, end='')
    return last_digit
