'''
Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Pentagonal	 	Pn=n(3n-1)/2	 	1, 5, 12, 22, 35, ...
Hexagonal	 	Hn=n(2n-1)	 	1, 6, 15, 28, 45, ...
It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
'''


def triangle(n):
    return n * (n + 1) / 2

def pent(n):
    return n * (3 * n - 1) / 2

def hex(n):
    return n * (2 * n - 1)


triangle_nums = {triangle(n) for n in range(1, 100000)}
pent_nums = {pent(n) for n in range(1, 100000)}
hex_nums = {hex(n) for n in range(1, 100000)}

for t in triangle_nums:
    if t in pent_nums and t in hex_nums:
        print t