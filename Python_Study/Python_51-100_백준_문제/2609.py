a, b = map(int, input().split())
num2, num3 = a, b
while b > 0:
    if a >= b:
        minx = a % b
        if minx == 0:
            num1 = b
            break
        else:
            a = b
            b = minx
    else:
        minx = b % a
        if minx == 0:
            num1 = a
            break
        else:
            b = a
            a = minx
print(num1)
print(num3*num2//num1)