A = int(input())
B = 2
while B < 10000000:
    if A == 1:
        break
    while A % B == 0:
        A = A / B
        print(B)
    B += 1
