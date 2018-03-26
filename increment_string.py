# Your job is to write a function which increments a string, to create a new string. If the string already ends with a
# number, the number should be incremented by 1. If the string does not end with a number the number 1 should be
# appended to the new string.

import re

def increment_string(strng):
    digits = re.search("\d+$", strng)
    if digits.group(0):
        new_string = strng[0:digits.start(0)] + str(int(digits.group(0)) +1).rjust(len(digits.group(0)), "0")
    else:
        new_string = strng + "1"
    return new_string
