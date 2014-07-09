"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""

#20 = 2^2 * 5
#19 = 19
#18 = 2 * 3^2
#17 = 17
#16 = 2^4
#15 = 3 * 5
#14 = 2 * 7
#13 = 13
#12 = 2 * 3^2
#11 = 11

#highest prime powers
#2^4
#3^2
#5
#7
#11
#13
#17
#19

factorList = [2, 2, 2, 2, 3, 3, 5, 7, 11, 13, 17, 19]
product = 1
for num in factorList:
    product *= num
print(product)

