#!/usr/bin/python3

# Check the function
multiple_returns = __import__("8-multiple_returns").multiple_returns

sentence = "At school, I learnt C!"
length, first_char = multiple_returns(sentence)
print("Length: {} - First character: {}".format(length, first_char))

length, first_char = multiple_returns("")
print("Length: {} - First character: {}".format(length, first_char))
