"""
project euler problem 1
https://projecteuler.net/index.php?section=problems&id=1

description:
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

alogrithm:
check each value between 1 and 1000 that are divisible by 3 or 5 and add to new list. Then sum all values in that list.

"""

import time
start = time.time()

multiples = []
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        multiples.append(i)

print 'solution 1 => ' + str(sum(multiples))
print 'execution time: ' + str(time.time() - start)
