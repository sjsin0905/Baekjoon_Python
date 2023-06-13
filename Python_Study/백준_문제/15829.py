num = int(input())
code = input()
num_list = []
total = 0
th = 1
for i in range(num):
    num_list.append(int(ord(code[i]) - 96))
    total += num_list[i] * th
    th *= 31
print(total)