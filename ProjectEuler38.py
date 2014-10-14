def concatProduct(x):
    s = ''
    i = 1
    while True:
        new_s = s + str(x * i)
        if len(new_s) > 9:
            return s
        s = new_s
        i += 1

def pandigital(low, high, num):
    if len(num) == (high - low + 1):
        s = str(num)
        for i in range(low, high + 1):
            if str(i) not in s:
                return False
        return True
    return False
    
highest = 0
for i in range(1, 9999):
    s = concatProduct(i)
    if int(s) > highest and pandigital(1, 9, s):
        print(s)
