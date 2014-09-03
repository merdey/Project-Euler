"""
The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
"""

n = 0
for i in range(1, 1001):
    n += i ** i

s = str(n)
print(s[-10:])
