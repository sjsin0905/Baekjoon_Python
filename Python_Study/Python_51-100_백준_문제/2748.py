a = int(input())
num_1 = 0
num_2 = 1
num = 1
for i in range(a-1):
    num = num_1 + num_2
    num_1 = num_2
    num_2 = num

print(num)
