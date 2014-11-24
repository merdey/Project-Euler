import itertools

def yield_pandigitals(length):
    """ Yields all 0 to length pandigitals 
        length is an integer between 1 and 9 """ 
    for pandigital in list(itertools.permutations(range(length + 1))):
        yield ''.join(map(str, pandigital))

primes = [2, 3, 5, 7, 11, 13, 17]
def subStringDivis(s):
    for i in range(7):
        n = int(s[1+i:4+i])
        if (n % primes[i]) != 0:
            return False
    return True

pandigitals = yield_pandigitals(9)
s = 0
for p in pandigitals:
    if subStringDivis(p):
        s += int(p)

print(s)
