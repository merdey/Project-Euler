'''
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''


def divisors(n):
    divs = set()
    for i in range(1, n / 2 + 1):
        if n % i == 0:
            divs.add(i)
    return divs


def is_abundant(n):
    return sum(divisors(n)) > n


stop = 28123 + 1
abundant_nums = [i for i in range(2, stop) if is_abundant(i)]

can_be_written = set()
for i, num1 in enumerate(abundant_nums):
    for j, num2 in enumerate(abundant_nums):
        can_be_written.add(num1 + num2)

res = 0
for n in range(stop):
    if n not in can_be_written:
        res += n

print res