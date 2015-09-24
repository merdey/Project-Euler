'''
A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]


greatest = 0
for i in range(999):
    for j in range(999):
        product = i * j
        if is_palindrome(product) and product > greatest:
            greatest = product
print greatest
