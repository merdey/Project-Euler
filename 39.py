'''
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximised?
'''


from collections import defaultdict
p_possibilities = defaultdict(set)


import math
for a in range(2, 500):
    for b in range(1, a):
        c = math.sqrt(a*a + b*b)
        if c % 1 == 0:
            p = a + b + c
            p_possibilities[p].add(frozenset([a, b, c]))


max_p = 0
max_poss = 0
for p, poss in p_possibilities.items():
    if len(poss) > max_poss:
        max_p = p
        max_poss = len(poss)

print max_p, max_poss