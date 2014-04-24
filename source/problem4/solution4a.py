"""
project euler problem # 4
https://projecteuler.net/index.php?section=problems&id=4

description:
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 =
 91  99.

Find the largest palindrome made from the product of two 3-digit numbers

algorithm:  
Start with the two largest 3 digit integer factors (999 * 999), decrement the second factor while keeping the first factor constant (999 * 999, 999 * 998, 999 * 997,... ), and multiply the two factors on each iteration. Once second factor reaches lowest 3 digit factor (100), then start again but decrement the first factor.  If the product of these two factors are a palidrome and is larger than currently stored palindrome (initial value == -1) then found it.

notes:
range => 999 - 100

algorithm for palidrome:
if current text is palidrome where first character and last character are same and inner text is also palidrome (where first and last character are also the same repeating the process), then the whole text is a palidrome

"""

import time
start = time.time()

def get_largest_palidrome(num_digits):
    not_a_palidrome = -1  # magic number!
    if num_digits < 1:
        return not_a_palidrome
    high_factor = int(str(9) * num_digits)
    low_factor = int('1' + (str(0) * (num_digits - 1)))
    factor1 = factor2 = high_factor
    palidrome = not_a_palidrome 

    def is_palidrome(text):
        if len(text) == 0 or len(text) == 1:
            return True
        return text[0] == text[-1] and is_palidrome(text[1:-1])

    def is_product_palidrome(factor1, factor2):
        product = factor1 * factor2
        if factor2 < low_factor:	# base case
            return not_a_palidrome
        if is_palidrome(str(product)):    # base case
            #print 'base #2-' + 'factor1: ' + str(factor1) + ' factor2: ' + str(factor2) + ' product: ' + str(factor1 * factor2)  # debug
            return product
        factor2 -= 1
        return is_product_palidrome(factor1, factor2)	#  recursion
        
    while(factor1 >= low_factor):
        new_palidrome = is_product_palidrome(factor1, factor2)
        if new_palidrome > palidrome:
            palidrome = new_palidrome
        factor1 -=1
        factor2 = high_factor

    return palidrome

# print "test example => " + str(get_largest_palidrome(num_digits = 2))
print 'solution 4 => ' + str(get_largest_palidrome(num_digits = 3))
print 'execution time:',time.time() - start
