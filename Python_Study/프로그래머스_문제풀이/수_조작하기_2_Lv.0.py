def solution(numLog):
    num = len(numLog)
    num_answer = []
    for i in range(1,num):
        num_an = numLog[i] - numLog[i-1]
        if num_an == 1:
            num_answer.append("w")
        elif num_an == -1:
            num_answer.append("s")
        elif num_an == 10:
            num_answer.append("d")
        else:
            num_answer.append("a")
    answer = "".join(map(str, num_answer))
    return answer