def solution(code):
    mode = 0
    ret = []
    count = 0
    for i in range(len(code)):
        if mode == 0:
            if code[i] == "1":
                mode = 1
                continue
            if i % 2 == 0:
                ret.append(code[i])
                count += 1
        else:
            if code[i] == "1":
                mode = 0
                continue
            if i % 2 == 1:
                ret.append(code[i])
                count += 1
    answer = ''.join(map(str, ret))
    if count == 0:
        answer = "EMPTY"
    return answer