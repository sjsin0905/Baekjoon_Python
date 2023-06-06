do = int(input())
for i in range(do):
    anw = input()
    score = 0
    sum = 0
    for j in range(len(anw)):
        if anw[j] == "O":
            score += 1
            sum += score
        elif anw[j] == "X":
            score = 0
    print(sum)
