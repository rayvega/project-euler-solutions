"""
project euler problem # 3
https://projecteuler.net/index.php?section=problems&id=3

description:
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?

algorithm:
Starting at 2, keep incrementing by one until find the next prime number. Once found, divide target number (600851475143) by this prime number, take the resulting quotient as the new target number, and repeat the process.

"""

import time
start = time.time()

def get_greatest_prime(number, previous_number = 1):
    if number == 1 or number == 0:
        return previous_number
    previous_number = number

    def get_next_prime_quotient(number):    
        next = 2
        while (True):
            if number % next == 0:
                # print 'prime ' + str(next)   # debug
                return number / next
            next += 1
    
    return get_greatest_prime(get_next_prime_quotient(number), previous_number)

# print 'test example => ' + str(get_greatest_prime(13195))	# test example: should equal 5, 7, 13 and 29.
print 'solution 3 => ' + str(get_greatest_prime(600851475143))
print 'execution time: ' + str(time.time() - start)
