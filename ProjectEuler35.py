"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

def rotations(s):
    rotations = []
    i = 1
    while i < len(s):
        rotated_s = s[-i:] + s[:-i]
        i += 1
        rotations.append(rotated_s)
    return rotations
        
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

primes = generatePrimes(1000000)
primes_set = set()
for prime in primes:
    primes_set.add(prime)

circular_prime_count = 0
for prime in primes:
    circular = True
    rots = rotations(str(prime))
    for r in rots:
        if int(r) not in primes_set:
            circular = False
    if circular:
        circular_prime_count += 1
print(circular_prime_count)
