"""
The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

def isPalindrome(n):
    s = str(n)
    reversedS = s[::-1]
    if( s == reversedS ):
        return True
    return False

def convertToBase2(n):
    #converts to binary representation and strips off leading '0b'
    return bin(n)[2:]

ans = 0
for num in range(1000000):
    if isPalindrome(num) and isPalindrome( convertToBase2(num) ):
        print(num)
        ans += num

print(ans)
        


