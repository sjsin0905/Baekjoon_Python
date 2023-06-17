n = int(input())
word = "*"
for i in range(1, n+1):
    print((word*i).rjust(n))
