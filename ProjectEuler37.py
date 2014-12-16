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

primes = generatePrimes(1000000)
prime_set = set(primes)

def isPrime(n):
    return n in prime_set

def truncatable(n):
    if n < 10:
        return False
    
    s = str(n)
    for i in range(1, len(s)):
        front = int(s[:i])
        back = int(s[-i:])
        if not isPrime(front) or not isPrime(back):
            return False
    return True

def findTruncatable():
    max_trunc = 11
    truncs = []
    for prime in primes[4:]:
        if truncatable(prime):
            truncs.append(prime)
            if len(truncs) == max_trunc:
                return truncs

truncs = findTruncatable()
print(truncs)
print(sum(truncs))

