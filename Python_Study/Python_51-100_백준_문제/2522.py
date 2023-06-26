n = int(input())

for i in range(n):
    print(("*" * i).rjust(n-1) + "*", sep="")
for i in range(n-2, -1, -1):
    print(("*" * i).rjust(n-1) + "*", sep="")