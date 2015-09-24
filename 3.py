'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

primes = [2]

def factor(n):
    factors = []
    while max(primes) < n:
        p = primes[-1]
        while n % p == 0:
            n = n / p
            factors.append(p)
        generateNextPrime()
    factors.append(n)
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
            return

print factor(600851475143)
        
