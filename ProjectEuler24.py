import itertools

p = itertools.permutations([0,1,2,3,4,5,6,7,8,9])
i = 0
for perm in p:
    i += 1
    if i == 1000000:
        print(perm)
