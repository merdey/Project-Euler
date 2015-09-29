'''
Surprisingly there are only three numbers that can be written as the
sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of
fifth powers of their digits.
'''


def is_sum_of_powers(n, pow):
    s = str(n)
    return sum(int(digit) ** pow for digit in s) == n

res = 0
for i in range(10, 1000000):
    if is_sum_of_powers(i, 5):
        res += i
print res