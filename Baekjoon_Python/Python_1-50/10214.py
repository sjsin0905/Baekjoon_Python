T = int(input())

for i in range(T):
    Y_score_total, K_score_total = 0, 0
    for i in range(9):
        y_score, k_score = map(int, input().split())
        Y_score_total += y_score
        K_score_total += k_score
    if K_score_total == Y_score_total:
        print("Draw")
    elif K_score_total > Y_score_total:
        print("Korea")
    elif Y_score_total > K_score_total:
        print("Yonsei")
