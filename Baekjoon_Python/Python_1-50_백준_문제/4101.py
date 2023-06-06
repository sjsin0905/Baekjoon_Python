a, b = 1, 1
while a != 0 and b != 0:
    a, b = map(int, input().split(" "))
    if a > b:
        result = "Yes"
    elif a == 0 and b == 0:
        break
    else:
        result = "No"
    print(result)
