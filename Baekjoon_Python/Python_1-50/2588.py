A = int(input())
B = input()

print(A * int(B[2]))

print(A * int(B[1]))

print(A * int(B[0]))

print(A * int(B))



"""
내가 푼 풀이

a = int(input())
b = int(input())

b_100 = b//100
b_10 = (b - (b_100*100))//10
b_1 = (b - (b_100*100))%10

print(a*b_1)
print(a*b_10)
print(a*b_100)
print((a*b_1)+(a*b_10*10)+(a*b_100*100))

"""
