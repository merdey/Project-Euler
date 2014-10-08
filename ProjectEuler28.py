last = 1
total = 1
size = 1001
for i in range(2, size, 2):
    for j in range(4):
        last += i
        total += last

print(total)
