"""
project euler problem # 5
https://projecteuler.net/index.php?section=problems&id=5

description:
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

algorithm:
use greatest common denominator (gcd) and lowest common multiples (lcm)
get lcm for n and n + 1. Then take lcm of n + 2 and previous lcm.  Keep incrementing n until 20.

"""

import time
start = time.time()

def get_smallest_number(max_num):
    def greatest_common_denominator(n, m):
        r = n % m
        if r == 0:
            return m
        return greatest_common_denominator(m, r)

    def lowest_common_multiples(n, m):
        return n * m / greatest_common_denominator(n, m)
    
    def find_small_number(n, lcm):
        # print 'n: ' + str(n) + ' lcm: ' + str(lcm)  # debug
        if n == max_num:
            return lcm
        return find_small_number(n + 1, lowest_common_multiples(n, lcm))

    return find_small_number(1, 2)

# print 'test example => ' + str(get_smallest_number(max_num = 10)) # expected value = 2520
print 'solution 5 => ' + str(get_smallest_number(max_num = 20))
print 'execution time: ' + str(time.time() - start)
