"""
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


def primeListGenerator(primesToGenerate):
    numOfPrimes = 1
    num = 3
    sieve = [2]
    while numOfPrimes < primesToGenerate:
        isPrime = True
        for prime in sieve:
            if num % prime == 0:
                isPrime = False
                break
        if isPrime:
            sieve.append(num)
            numOfPrimes += 1
        num += 1
            
    return sieve
 
print(primeListGenerator(10001)[10000])
