#!/usr/bin/python3
Rectangle = __import__('3-rectangle').Rectangle

my_rectangle = Rectangle(height=5)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print(str(my_rectangle))  # Prints the string representation of rectangle
print(repr(my_rectangle))  # Prints the official (address) representation

print('--')

my_rectangle.width = 10
my_rectangle.height = 3

print(my_rectangle)  # Prints the string representation of rectangle
print(repr(my_rectangle))  # Prints the official (address) representation

