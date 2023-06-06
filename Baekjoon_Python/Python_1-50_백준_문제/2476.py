person = int(input())
price = [0]*person
for i in range(0, person):
    a, b, c = map(int, input().split(" "))
    s = [0]*3
    s[0] = a
    s[1] = b
    s[2] = c
    s.sort()
    if a == b and b == c:
        price[i] = 10000 + (a * 1000)
    elif (a == b or b == c) or c == a:
        if a == b:
            price[i] = 1000 + (a * 100)
        elif b == c:
            price[i] = 1000 + (b * 100)
        elif a == c:
            price[i] = 1000 + (a * 100)
    else:
        price[i] = s[2] * 100
price.sort(reverse=True)
print(price[0])