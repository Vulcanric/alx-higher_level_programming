#!/usr/bin/python3

def uppercase(str):
    i = 0
    while i < len(str):
        # if char at index is lower
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            # Convert to uppercase ascii number
            upper = ord(str[i]) - 32  # 'a' - 32 = 'A' and so on ...

        # otherwise let the char remain the same
        else:
            upper = ord(str[i])

        # Print the ascii upper letter from ascii number
        print("{}".format(chr(upper)), end='')
        i += 1

    print("{}".format('\n'), end='')  # print newline after all done
