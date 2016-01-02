def formula(n, a, b):
    return (n ** 2) + (a * n) + b


primes = [2]
for i in range(3, 100000):
    for p in primes:
        if i % p == 0:
            break
    else:
        primes.append(i)

primes = set(primes)
def is_prime(n):
    return n in primes


max_run = 0
max_values = (0, 0)
for a in range(-999, 1000):
    for b in range(-999, 1000):
        n = 0
        current_run = 0

        while is_prime(formula(n, a, b)):
            n  += 1
            current_run += 1

        if current_run > max_run:
            max_run = current_run
            max_values = (a, b)

print max_values[0] * max_values[1]