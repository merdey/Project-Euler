"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
max_num = 100000000
collatz_cache = [0] * max_num
collatz_cache[1] = 1

def collatz(n):
    original_n = n
    length = 0
    while collatz_cache[n] == 0:
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = (3 * n) + 1
        length += 1
        while n > max_num:
            if n % 2 == 0:
                n = int(n / 2)
            else:
                n = (3 * n) + 1
            length += 1
    collatz_cache[original_n] = length + collatz_cache[n]

for i in range(2, 1000000):
    collatz(i)

print( collatz_cache.index(max(collatz_cache)) )


