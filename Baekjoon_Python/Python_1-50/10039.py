count = 0
a = [0, 0, 0, 0, 0]
for i in range(5):
    a[i] = int(input())
    if a[i] < 40:
        a[i] = 40
    count = count + a[i]

print(int(count / 5))
