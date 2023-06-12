A = int(input())
B = 2
while B < 10000000:
    if A == 1:
        break
    while A % B == 0:
        A = A / B
        print(B)
    B += 1


"""
다른사람 풀이

n = int(input())
i = 2
while n!=1:
    if n%i == 0:
        print(i)
        n = n/i
    else:
        i+=1

내가 짠 코드보다 더 빠름


"""