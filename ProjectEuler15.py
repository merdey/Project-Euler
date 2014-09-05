"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
"""

a = 20
b = 20
n = a + b
k = b

def nChooseK(n, k):
    return factorial(n) / ( factorial( n - k ) * factorial(k) )

def factorial(n):
    for i in range(1, n):
        n = n * i
    return n

print( nChooseK(40, 20) )
