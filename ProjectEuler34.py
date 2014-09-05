"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

def digitFactorialSum(n):
    s = str(n)
    factSum = 0
    for digit in s:
        factSum += factorial( int(digit) )
    return factSum

def factorial(n):
    if n == 0:
        return 1
    for i in range(1, n):
        n = n * i
    return n

ans = 0
for i in range(10, 3000000):
    if digitFactorialSum(i) == i:
        ans += i
print(ans)
    
