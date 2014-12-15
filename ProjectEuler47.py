def generatePrimes(upTo):
    primes = [1] * upTo
    for i in range(2, int(upTo / 2)):
        if primes[i]:
            j = i * 2
            while j < upTo:
                primes[j] = 0
                j += i
    primes_list = []
    for i in range(len(primes)):
        if primes[i]:
            primes_list.append(i)
    return primes_list[2:]

primes = generatePrimes(250000)
print('primes generated')

def factor(n):
    prime_factors = {}
    i = 0
    while n > 1:
        p = primes[i]
        while n % p == 0:
            if p in prime_factors:
                prime_factors[p] += 1
            else:
                prime_factors[p] = 1
            n = n / p
        i += 1
    return prime_factors

def consecutiveDistinct(length):
    i = 2
    while True:
        factors = set()
        for n in range(i, i+length):
            facts = factor(n)
            for f in facts:
                factors.add(f * facts[f])
        if len(factors) == (length ** 2):
            return i
        i += 1

print(consecutiveDistinct(4))

