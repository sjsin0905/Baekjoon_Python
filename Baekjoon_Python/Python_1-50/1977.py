M = int(input())
N = int(input())
count = 1
num_sum = 0
num_list = []
while True:
    if count*count < M:
        count += 1
    elif M <= count*count <= N:
        num_list.append(count*count)
        num_sum += count*count
        count += 1
    elif count * count > N:
        break
if num_sum > 0:
    print(num_sum)
    print(num_list[0])
else:
    print("-1")
