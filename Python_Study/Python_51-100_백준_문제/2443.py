n = int(input())

for i in range(n-1, -1, -1):
    print(("*" * i).rjust(n-1) + "*" + "*" * i, sep="")
