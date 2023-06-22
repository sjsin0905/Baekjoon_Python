hak = int(input())

for i in range(hak):
    total = 0
    G_sum = 0.0
    num = int(input())
    for j in range(num):
        C, G = map(float, input().split())
        sum = C * G
        G_sum += sum
        total += C
        total = int(total)
        ttotal = G_sum / total
    print(f"{total} {round(ttotal, 1)}")