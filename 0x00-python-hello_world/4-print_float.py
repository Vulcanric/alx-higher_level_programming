#!/usr/bin/python3
number = 3.14159

if not isinstance(number, float):
    print(f"Float: {number}")
elif number < 0:
    print(f"Float: {number: .2f}")
else:
    print(f"Float:{number: .2f}")
