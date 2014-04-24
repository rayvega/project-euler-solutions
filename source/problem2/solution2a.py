"""
project euler problem 2
https://projecteuler.net/index.php?section=problems&id=2

description:
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

algorithm:
calculate each term of fibonacci series starting at zero(0) by adding the current term with the previous one. Place each new term (i.e. sum) in a growing list of fib terms. Stop building the list once the current term is greater than 4 million.  Then sum the list after filtering for only even numbers (i.e. removing all odd numbers).

"""

import time
start = time.time()

def fib(terms):
    # print 'term1: ' + str(terms[-2]) + ' term2: ' + str(terms[-1])  # debug
    sum = terms[-2] + terms[-1]	
    if sum > 4 * pow(10, 6):  # 4 million
        return terms
    terms.append(sum)
    return fib(terms)

print 'solution 2 => ' + str(sum([term for term in fib([0,1]) if term % 2 == 0]))
print 'execution time: ' + str(time.time() - start)
