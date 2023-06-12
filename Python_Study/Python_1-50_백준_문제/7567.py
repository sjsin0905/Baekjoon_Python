B = input()
h = 10
if B[0] == "(":
    for i in range(1, len(B)):
        if B[i-1] == "(" and B[i] == "(":
            h += 5
        elif B[i-1] == ")" and B[i] == "(":
            h += 10
        elif B[i-1] == "(" and B[i] == ")":
            h += 10
        elif B[i-1] == ")" and B[i] == ")":
            h += 5
elif B[0] == ")":
    for i in range(1, len(B)):
        if B[i-1] == "(" and B[i] == "(":
            h += 5
        elif B[i-1] == ")" and B[i] == "(":
            h += 10
        elif B[i-1] == "(" and B[i] == ")":
            h += 10
        elif B[i-1] == ")" and B[i] == ")":
            h += 5
print(h)