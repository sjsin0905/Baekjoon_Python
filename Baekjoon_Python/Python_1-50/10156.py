K, N, M = map(int, input().split(" "))
price = K * N
mm = K * N - M
if mm >= 0:
    print(mm)
elif mm < 0:
    print("0")