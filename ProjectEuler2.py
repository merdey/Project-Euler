def EvenFibSum():
    ans = 0
    prev = 1
    current = 1
    while current <= 4000000:
        if current % 2 == 0:
            ans += current
        current, prev = current + prev, current
    return ans

print(EvenFibSum())
