n = int(input())

for i in range(n):
    s = int(input())
    n = int(input())
    sum_qp = 0
    for j in range(n):
        q, p = map(int, input().split())
        sum_qp += q * p
    print(sum_qp + s)