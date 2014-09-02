"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def generateTriple(m, n):
    a = m**2 - n**2
    b = 2 * m * n
    c = m**2 + n**2
    return [a, b, c]

def product(a):
    prod = 1
    for i in a:
        prod *= i
    return prod

for m in range(2, 500):
    for n in range(1, m):
        triple_sum = sum( generateTriple(m, n) )
        for k in range(1, 50):
            if triple_sum * k == 1000:
                print( product( generateTriple(m, n) ) )
                
