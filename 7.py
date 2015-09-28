'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

primes = [2]
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

while len(primes) < 10001:
    generateNextPrime()

print primes[-1]