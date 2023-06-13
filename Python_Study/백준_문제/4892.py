count = 1
while True:
    n0 = int(input())
    if n0 == 0:
        break
    n1 = 3 * n0
    if n1 % 2 == 0:
        n2 = n1 / 2
        print(f"{count}. even", end=" ")
    else:
        n2 = (n1 + 1) / 2
        print(f"{count}. odd", end=" ")
    n3 = 3 * n2
    n4 = n3 // 9
    print(int(n4))
    count += 1
