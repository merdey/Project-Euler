"""
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""

def concatProduct(x):
    s = ''
    i = 1
    while True:
        new_s = s + str(x * i)
        if len(new_s) > 9:
            return s
        s = new_s
        i += 1

def pandigital(low, high, num):
    if len(num) == (high - low + 1):
        s = str(num)
        for i in range(low, high + 1):
            if str(i) not in s:
                return False
        return True
    return False
    
highest = 0
for i in range(1, 9999):
    s = concatProduct(i)
    if int(s) > highest and pandigital(1, 9, s):
        print(s)
