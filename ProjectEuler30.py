"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

def sum_fifth_powers(n):
    res = 0
    s = str(n)
    for digit in s:
        res += int(digit) ** 5
    return res

ans = 0
not_found_in = 0
cutoff = 1000000
n = 2
while not_found_in < cutoff:
    if n == sum_fifth_powers(n):
        ans += n
        not_found_in = 0
    else:
        not_found_in += 1
    n += 1

print(ans)
    
    
    
