def generatePrimes(upTo):
    sieve = [1] * (upTo + 1)
    for i in range(2, len(sieve)):
        if sieve[i]:
            for j in range(i * 2, upTo + 1, i):
                sieve[j] = 0
    return sieve

def arePermutations(seq):
    key = lowestPermutation(seq[0])
    for n in seq[1:]:
        if lowestPermutation(n) != key:
            return False
    return True

def lowestPermutation(num):
    s = str(num)
    return (''.join(sorted(s)))

sieve = generatePrimes(10000)
primes = set()
for i in range(1000, len(sieve)): #only want to work with 4 digit primes
    if sieve[i]:
        primes.add(i)
        
sums = []
for prime in primes:
    difference = 10000 - prime
    for a in range(1, int(difference / 2)):
        seq = [prime]
        seq.append(prime + a)
        seq.append(prime + (2 * a))
        are_prime = True
        for n in seq:
            if n not in primes:
                are_prime = False
        if are_prime and arePermutations(seq):
            if sum(seq) not in sums: #ignore permutations of sequence
                print(seq)
                input()
            
