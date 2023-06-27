import sys
input = sys.stdin.readline

n = int(input())
sum = 0
for i in range(n):
    r = int(input())
    sum += (r - 1)

print(sum + 1)