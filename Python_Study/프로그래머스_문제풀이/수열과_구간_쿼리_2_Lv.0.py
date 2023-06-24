def solution(arr, queries):
    answer = []
    for i in queries:
        a = i[0]
        b = i[1]
        c = i[2]
        min = 10000000000000
        temp = 100100000000000000
        for j in range(a, b+1):
            if arr[j] > c:
                temp = arr[j]
            if temp <= min:
                min = temp
        if min == 10000000000000:
            min = -1
        answer.append(min)
    return answer