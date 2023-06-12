a, b, c = map(int, input().split())
s = [0]*3
s[0] = a
s[1] = b
s[2] = c
s.sort()
price = 0

if a == b and b == c:
    price = 10000 + (a * 1000)
elif (a == b or b == c) or c == a:
    if a == b:
        price = 1000 + (a * 100)
    elif b == c:
        price = 1000 + (b * 100)
    elif a == c:
        price = 1000 + (a * 100)
else:
    price = s[2] * 100

print(price)