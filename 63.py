'''
How many n-digit positive integers exist which are also an nth power?
'''

res = 0
for i in range(1, 1000):
    for e in range(1, 100):
        n = i ** e
        if len(str(n)) == e:
            res += 1
        
print res