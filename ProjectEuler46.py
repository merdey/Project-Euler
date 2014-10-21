"""
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""

def generatePrimes(upTo):
    sieve = [1] * (upTo + 1)
    for i in range(2, len(sieve)):
        if sieve[i]:
            for j in range(i * 2, upTo + 1, i):
                sieve[j] = 0
    primes = []
    for i in range(2, len(sieve)):
        if sieve[i]:
            primes.append(i)
    return primes

primes = generatePrimes(10000)
primes_set = set()
for prime in primes:
    primes_set.add(prime)

generated_composites = set()
for p in primes:
    for x in range(1, 1000):
        c = p + (2 * x**2)
        if c % 2 != 0: #keep composite list smaller by only including odds
            generated_composites.add(c)

#composite number is number > 1 that isnt prime
for i in range(3, 100000000, 2):
    if i not in primes:
        if i not in generated_composites:
            print(i)
            break

    
