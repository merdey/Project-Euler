import math

def generateDivisors(num):
    divs = set()
    divs.add(1)
    for i in range(2, int(num / 2)):
        if num % i == 0:
            divs.add(i)
            divs.add(num / i)
    return divs

abundant_nums = []
for i in range(12, 28124):
    divs = generateDivisors(i)
    if sum(divs) > i:
        abundant_nums.append(i)
print('hello')
abundant_sums = set()
for i in range(len(abundant_nums)):
    for j in range(i, len(abundant_nums)):
        s = abundant_nums[i] + abundant_nums[j]
        if s < 28124:
            abundant_sums.add(abundant_nums[i] + abundant_nums[j])
print('world')

non_abundant_sum_total = 0 
for i in range(1, 28124):
    if i not in abundant_sums:
        non_abundant_sum_total += i
print(non_abundant_sum_total)
        
        
