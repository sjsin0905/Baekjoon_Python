i = int(input())
case = [0]
for do in range(0, i):
    j, k = input().split(" ")
    case.append(int(j))
    case.append(int(k))
sum = [0]
for p in range(1, i*2, 2):
    sum.append(int(case[p]) + int(case[p+1]))
for a in range(1, i+1):
    print("Case #{0}: {1}".format(a, sum[a]))
