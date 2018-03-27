# Find the number of divisors of a positive integer n.
# Random tests go up to n = 500000.

import math

def divisors(n):
    count = 0
    for e in range(1, int(math.sqrt(n))+1):
        if n % e == 0:
            count += 1
            if n / e != e:
                count += 1
    return count