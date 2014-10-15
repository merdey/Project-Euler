"""
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
"""

def determineWordValue(word):
    res = 0
    for letter in word:
        res += ord(letter) - 64
    return res

def triangle(n):
    return int(n * (n + 1) / 2)

triangle_nums = set()
for i in range(1, 100):
    triangle_nums.add(triangle(i))

file = open('words.txt', 'r')
words = file.read().split(',')
triangle_words = 0
for word in words:
    if determineWordValue(word[1:-1]) in triangle_nums:
        triangle_words += 1
print(triangle_words)
