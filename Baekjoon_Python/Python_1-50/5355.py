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
