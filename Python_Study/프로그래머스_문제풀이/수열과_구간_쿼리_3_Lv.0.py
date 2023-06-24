def solution(arr, queries):
    for i in queries:
        a = i[0]
        b = i[1]
        temp = 0
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp
    return arr