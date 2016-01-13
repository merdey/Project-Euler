'''
Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?
'''

primes = []
for i in range(2, 100000):
    is_prime = True
    for p in primes:
        if i % p == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)

def num_prime_divs(n):
    res = 0
    for p in primes:
        if p < n and n % p == 0:
            res += 1
    return res


consecutive = 0
i = 647
while True:
    p_divs = num_prime_divs(i)
    if p_divs == 4:
        consecutive += 1
        if consecutive == 4:
            print i - 3
            break
    else:
        consecutive = 0

    i += 1
