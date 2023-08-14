#!/usr/bin/python3

# prints the ascii alphabets in lowercase
# except from letter 'e' and 'q'
for i in range(97, 123):
    if chr(i) != 'e' and chr(i) != 'q':
        print("{}".format(chr(i)), end='')
