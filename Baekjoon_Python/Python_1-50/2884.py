H, M = map(int, input().split(" "))

if M - 45 >= 0:
    print(H, M - 45, sep=" ")
elif M - 45 < 0:
    if H - 1 >= 0:
        print(H-1, M + 15, sep=" ")
    elif H - 1 < 0:
        print(H + 23, M + 15, sep=" ")