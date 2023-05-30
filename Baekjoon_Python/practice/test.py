arr = [*map(int, input().split())]
result = []
arr.sort()
arr_set = set(arr)
for i in arr_set:
    if arr.count(i) > 1:
        result.append(arr.count(i))
if len(result) == 0:
    result.append(-1)
print(result)
