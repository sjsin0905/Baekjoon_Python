# @는 3을 곱하고, %는 5를 더하며, #는 7을 빼는 연산자이

g = "@"
n = "%"
m = "#"
a = []
i = int(input())
for r in range(0, i):
    a.append(input())
    b = a[0].split()
    num = float(b[0])
    for k in b:
        if k == "@":
            num = num * 3
        elif k == "%":
            num = num + 5
        elif k == "#":
            num = num - 7
    print("{0:.2f}".format(num))
    a.clear()
