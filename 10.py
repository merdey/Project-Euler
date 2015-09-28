'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

two_million = 2000000
possible_primes = set(range(2, two_million))

n = 2
while n < two_million:
    not_prime = n + n
    while not_prime < two_million:
        try:
            possible_primes.remove(not_prime)
        except:
            pass
        not_prime += n
    n += 1


print sum(possible_primes)