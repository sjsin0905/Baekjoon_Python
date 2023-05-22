i = int(input())
for a in range(i):
    r, e, c = map(int, input().split())
    if e - r > c:
        print("advertise")
    elif e - r == c:
        print("does not matter")
    elif e - r < c:
        print("do not advertise")