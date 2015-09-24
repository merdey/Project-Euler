'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
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
