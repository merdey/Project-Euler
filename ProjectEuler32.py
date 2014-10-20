"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

def isPandigital(s, n):
    digits = set()

    #correct length
    if len(s) != n:
        return False
    #no repeats
    for digit in s: 
        if digit in digits:
            return False
        digits.add(int(digit))
    #all 1 to n
    for i in range(1, n+1):
        if i not in digits:
            return False
        
    return True

pandigital_products = set()
for a in range(1, 999):
    for b in range(10, 9999):
        p = a * b
        s = str(a) + str(b) + str(p)
        if isPandigital(s, 9):
            pandigital_products.add(p)
            print(a, b, p, s)
print(pandigital_products)
print(sum(pandigital_products))
    
