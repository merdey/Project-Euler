"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def isPalindrome(num):
    num = str(num)
    for i in range(int(len(num) / 2)):
        if num[i] != num[-1 - i]:
            return False
    return True

largest = 0
for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        num = i * j
        if isPalindrome(num) and num > largest:
            largest = num

print(largest)
        

