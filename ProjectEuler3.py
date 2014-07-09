"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def primeListGenerator(upTo):
    sieve = [2]
    for i in range(3, upTo):
        isPrime = True
        for prime in sieve:
            if i % prime == 0:
                isPrime = False
                break
        if isPrime:
            sieve.append(i)
    return sieve
            
def factorOutPrimes(num):
    primeGenerator(10000)
    #print(sieve)
    for prime in sieve:
        while num % prime == 0:
            num /= prime
        if num == 1:
            return prime
    return num

print(factorOutPrimes(600851475143))
