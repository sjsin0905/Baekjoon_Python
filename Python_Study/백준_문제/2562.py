num_list = {}
for i in range(9):
    num = int(input())
    num_list[num] = i+1
num_list_sort = sorted(num_list.items(), key=lambda x: x[0])
print(num_list_sort[8][0])
print(num_list_sort[8][1])
