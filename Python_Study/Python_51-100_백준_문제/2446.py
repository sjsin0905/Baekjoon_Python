n = int(input())

for i in range(1, n+1):
    print(("*" * (n-i)).rjust(n-1) + "*" + "*" * (n-i), sep="")
for i in range(1, n):
    print(("*" * i).rjust(n-1) + "*" + "*" * i, sep="")