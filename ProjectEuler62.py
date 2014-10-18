"""
The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
"""

def lowestPermutation(num):
    s = str(num)
    return (''.join(sorted(s)))

maxToCube = 10000

cubes = []
for i in range(1, maxToCube):
    cubes.append(i ** 3)

perms = {}
for cube in cubes:
    if lowestPermutation(cube) in perms:
        key = perms[lowestPermutation(cube)]
        key[0] += 1
        key[1] = min(key[1], cube)
        if key[0] == 5:
            print(key[1])
    else:
        perms[lowestPermutation(cube)] = [1, cube]
