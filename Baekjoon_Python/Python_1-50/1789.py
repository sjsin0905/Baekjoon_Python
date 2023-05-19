S = int(input())
count = 0
N = 1
while count <= S:
    count = count + N
    if count > S:
        print(N-1)
    N += 1
