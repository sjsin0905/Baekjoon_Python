T = int(input())

for i in range(T):
    N = int(input())
    sum = {}
    total = []
    for k in range(N):
        name, many = input().split()
        many = int(many)
        sum[many] = name
    for item in sum.keys():
        total.append(item)
    total.sort(reverse=True)
    print(sum.get(total[0]))