# Module 8 - Python program - greater_than function
# Author: Kaleb Whybrew
#
# This program defines a function that compares two numbers and
# returns True if the first is greater than the second, otherwise
# False. The main section then prints a full sentence about the result.
# (Python identifiers can not contain a hyphen, so the function is
#  named greater_than with an underscore.)


def greater_than(x, y):          # user-defined function with two parameters
    if x > y:                    # check whether x is greater than y
        return True              # x is greater, so return True
    else:
        return False             # x is not greater, so return False


# ----- main program -----
a = 2                            # first number
b = 3                            # second number
result = greater_than(a, b)      # call the function and store the True/False result

# convert a, b, and result to strings so they can join the sentence
print("The statement " + str(a) + " is greater than " + str(b) + " is " + str(result))
