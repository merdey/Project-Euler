'''
Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
'''


def is_palindrome(s):
    return s == s[::-1]


res = 0
for i in range(1, 1000000):
    s = str(i)
    b = bin(i)[2:]
    if is_palindrome(s) and is_palindrome(b):
        res += i
print res
