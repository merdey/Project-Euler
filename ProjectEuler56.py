"""
A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
"""

def sumDigits(n):
    s = str(n)
    digitSum = 0
    for digit in s:
        digitSum += int(digit)
    return digitSum

greatestDigitSum = 0
for a in range(100):
    for b in range(100):
        digitSum = sumDigits(a ** b)
        greatestDigitSum =  max(digitSum, greatestDigitSum)
print(greatestDigitSum)
    
    
