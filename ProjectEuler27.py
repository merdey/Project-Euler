def generatePrimes(upTo):
    sieve = [1] * (upTo + 1)
    for i in range(2, len(sieve)):
        if sieve[i]:
            for j in range(i * 2, upTo + 1, i):
                sieve[j] = 0
    return sieve

sieve = generatePrimes(1000)
primes = set()
for i in range(2, len(sieve)):
    if sieve[i]:
        primes.add(i)

greatest_product = 0
greatest_count = 0
for a in range(-999, 1000):
    for b in range(-999, 1000): #can optimize by only testing primes, when n == 0, b must be prime or equation wont be prime
        prime_count = 0
        n = 0
        while (n**2 + a * n + b) in primes:
            prime_count += 1
            n += 1
        if prime_count > greatest_count:
            greatest_count = prime_count
            greatest_product = a * b
print(greatest_product)
        
