"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


def primeListSum(upTo):
    sieve = []
    for i in range(upTo):
        sieve.append(True)

    for i in range(2, upTo):
        if (not sieve[i]):
            continue
        else:
            j = i + i
            while (j < upTo):
                sieve[j] = False
                j += i

    s = 0
    for i in range(2, upTo):
        if sieve[i]:
            s += i

    return s

print(primeListSum(2000000))
