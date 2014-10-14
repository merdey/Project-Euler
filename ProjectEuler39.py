"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""

import math

counts = [0] * 1001
for a in range(1, 1000):
    for b in range(1, 1000):
        c = math.sqrt(a ** 2 + b ** 2)
        if c % 1 == 0 and int(a + b + c) <= 1000:
            counts[int(a + b + c)] += 1

print(counts.index(max(counts)))
