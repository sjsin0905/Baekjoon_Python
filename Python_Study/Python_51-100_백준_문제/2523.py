n = int(input())

for i in range(n):
    print("*" + "*" * i, sep="")
for i in range(n-2, -1, -1):
    print("*" + "*" * i, sep="")