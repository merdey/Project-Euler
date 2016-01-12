'''
Using words.txt, a 16K text file containing nearly two-thousand
common English words, how many are triangle words?
'''


def tri_num(n):
    return n * (n + 1) / 2


def letter_sum(word):
    s = 0
    for letter in word:
        s += ord(letter) - 64
    return s


triangle_nums = set()
for i in range(1, 200):
    t = tri_num(i)
    triangle_nums.add(t)

with open('p042_words.txt', 'r') as f:
    words = f.read().split(',')
    words = [w[1:-1] for w in words]  # strip quotes

res = 0
for word in words:
    if letter_sum(word) in triangle_nums:
        res += 1
print res
