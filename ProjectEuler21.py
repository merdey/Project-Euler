"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

import math

def generateDivisors(n):
    divisors = set([1])
    for i in range(2,  int(math.sqrt(n) + 1) ):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n / i)
    return divisors

def sumDivisors(n):
    divisors = generateDivisors(n)
    return sum(divisors)

amicable_nums = set()
for i in range(2, 10000):
    divisor_sum_i = sumDivisors(i)
    if divisor_sum_i != i:
        divisor_sum_j = sumDivisors(divisor_sum_i)
        if divisor_sum_j == i:
            amicable_nums.add(i)
            amicable_nums.add(divisor_sum_i)
        
print(amicable_nums)
print( sum( amicable_nums ) )
