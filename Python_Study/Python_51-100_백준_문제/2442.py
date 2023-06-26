n = int(input())

for i in range(n):
    print(("*" * i).rjust(n-1) + "*" + "*" * i, sep="")

