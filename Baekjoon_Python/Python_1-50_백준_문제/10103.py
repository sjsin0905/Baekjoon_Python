n = int(input())
c, y = 100, 100
for i in range(n):
    c_d, y_d = map(int, input().split())
    if c_d == y_d:
        continue
    elif c_d > y_d:
        y -= c_d
    elif y_d > c_d:
        c -= y_d
print(c)
print(y)