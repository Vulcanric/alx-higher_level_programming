#!/usr/bin/python3
""" 16-main """
from models.rectangle import Rectangle


list_input = [
        {'id': 89, 'width': 10, 'height': 4},
        {'id': 7, 'width': 1, 'height': 7}
    ]
print(list_input)
print(type(list_input))
print()

list_json_string = Rectangle.to_json_string(list_input)
print(list_json_string)
print(type(list_json_string))
print()

list_output = Rectangle.from_json_string(list_json_string)
print(list_output)
print(type(list_output))
