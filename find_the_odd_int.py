# Given an array, find the int that appears an odd number of times.
# There will always be only one integer that appears an odd number of times.


def find_it(seq):
    my_set = set()
    for e in seq:
        if e in my_set:
            my_set.remove(e)
        else:
            my_set.add(e)
    return my_set.pop()
