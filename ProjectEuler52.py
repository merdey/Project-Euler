"""
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""

def multiplePermutation(n, multiplier):
    m = n * multiplier
    if count_nums(n) == count_nums(m):
        return True
    return False

def count_nums(n):
    counts = {}
    s = str(n)
    for digit in s:
        if digit in counts:
            counts[digit] += 1
        else:
            counts[digit] = 1
    return counts

multiple_max = 6
search_max = 10000000
for num in range(1, search_max):
    for multiplier in range(1, multiple_max + 1):
        if not multiplePermutation(num, multiplier):
            break
        elif multiplier == multiple_max:
            print(num)
            print(num * 2)
    
    
