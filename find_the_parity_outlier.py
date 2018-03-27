# You are given an array (which will have a length of at least 3, but could be very large) containing integers.
# The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single
# integer N. Write a method that takes the array as an argument and returns this "outlier" N.

def find_outlier(integers):
    if (integers[0] % 2 + integers[1] % 2 + integers[2] % 2) > 1:
        for e in integers:
            if (e % 2) == 0:
                return e
    else:
        for e in integers:
            if (e % 2) == 1:
                return e