"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
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

def isPandigital(s):
    digits = set()
    n = len(s)
    #no repeats
    for digit in s: 
        if digit in digits:
            return False
        digits.add(int(digit))
    #all 1 to n
    for i in range(1, n+1):
        if i not in digits:
            return False
        
    return True

primes = generatePrimes(10000000)
greatest = 0
for p in primes:
    if isPandigital(str(p)):
        greatest = max(greatest, p)
print(greatest)
