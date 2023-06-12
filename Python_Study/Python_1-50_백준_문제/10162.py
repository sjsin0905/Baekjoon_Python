T = int(input())
a, b, c = 0, 0, 0
if T % 10 != 0:
    print("-1")
else:
    while True:
        if T >= 300:
            a += 1
            T -= 300
        else:
            break
    while True:
        if T >= 60:
            b += 1
            T -= 60
        else:
            break
    while True:
        if T >= 10:
            c += 1
            T -= 10
        else:
            break
    print(f"{a} {b} {c}")