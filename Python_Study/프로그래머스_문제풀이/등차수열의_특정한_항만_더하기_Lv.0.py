def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        if included[i]:
            answer_p = a + d * i
            answer += answer_p
    return answer