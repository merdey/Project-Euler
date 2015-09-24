'''
2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all
of the numbers from 1 to 20?
'''

from collections import defaultdict

primes = [2]
def factor(n):
    factors = defaultdict(int)
    i = 0
    while primes[i] < n:
        p = primes[i]
        while n % p == 0:
            n = n / p
            factors[p] += 1

        i += 1
        if len(primes) <= i:
            generateNextPrime()

    factors[n] = 1
    return factors


def generateNextPrime():
    n = max(primes)
    while True:
        n += 1
        for p in primes:
            if n % p == 0:
                break
        else:
            primes.append(n)
            return n

res = 1
factored = {}
for i in range(1, 21):
    factored[i] = factor(i)

for p in primes:
    greatest_power = max([factored[i][p] for i in range(1, 21)])
    res *= (p ** greatest_power)

print res
