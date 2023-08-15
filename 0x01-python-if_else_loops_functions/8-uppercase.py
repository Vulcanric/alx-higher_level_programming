#!/usr/bin/python3

def uppercase(str):
    i = 0
    while i < len(str):
        # if char at index is lower
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            # Convert to uppercase ascii number
            upper = ord(str[i]) - 32  # 'a' - 32 = 'A' and so on ...
            # Print the ascii upper letter from ascii number
            print(chr(upper), end='')

        # otherwise print the char as it is
        else:
            print(str[i], end='')
        i += 1
    print()  # print newline after all done
