"""
project euler problem # 5
https://projecteuler.net/index.php?section=problems&id=5

description:
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

algorithm:
start with 1 and increment by 1 until reach n where n is the solution number. For each number, divide by each value between 1 and 20 checking if all have remainder of zero.  Repeat this until find a number where this is true and then stop.

"""

import time
start = time.time()

def get_smallest_number(max_num):
    # print 'start with max_num == ' + str(max_num) + ' ...' # debug
    smallest_number = 1 
    is_evenly_divisible = True
    while(True):
        #print smallest_number # debug
        for i in range(1, max_num):
            if smallest_number % i != 0:
                is_evenly_divisible = False
                break
            is_evenly_divisible = True
        if is_evenly_divisible:
            return smallest_number
        smallest_number += 1

# print 'test example solution => ' + str(get_smallest_number(max_num = 10)) # expected value = 2520
print 'solution 5 => ' + str(get_smallest_number(max_num = 20))  # warning: takes too long
print 'execution time: ' + str(time.time() - start)
