"""
The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""


count = 0
for n  in range(1, 1000):
    for power in range(1, 100):
        s = str(n ** power)
        if len(s) == power:
            count += 1
            print(n, power, s, count)
            
            
