# n = 9789690303392599179037
n = 100000
for i in range(1, n):
    while i != 1:
        if i % 2 == 0:
            i /= 2
        else:
            i = 3 * i + 1
    else:
        continue

else:
    print("all True")
