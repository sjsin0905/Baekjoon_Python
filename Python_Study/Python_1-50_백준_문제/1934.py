T = int(input())
for i in range(T):
    A, B = map(int, input().split())
    A1 = A
    B1 = B
    N = 1
    if A == B:
        print(A)
    elif A > B:
        while N != 0:
            N = A % B
            if N == 0:
                GCD = B
                break
            else:
                A = N
                K = A
                A = B
                B = K
        print(int(A1 * B1 / GCD))
    else:
        while N != 0:
            N = B % A
            if N == 0:
                GCD = A
                break
            else:
                B = N
                K = B
                B = A
                A = K
        print(int(A1 * B1 / GCD))









"""
풀었지만 시간초과

T = int(input())
for i in range(T):
    A, B = map(int, input().split())
    num = [0, 0]
    num[0] = A
    num[1] = B
    num.sort()
    if A == B:
        print(A)
    elif num[1] % num[0] == 0:
        print(num[1])
    else:
        K = num[1]
        count = 1
        while K % num[0] != 0:
            count += 1
            K = num[1] * count
        print(K)
"""


"""
최대공약수(GCD) - 두 수를 공통으로 나눌 수 있는 수 중 제일 작은 수
[유클리드 알고리즘]
a/b를 후 나머지를 a에 저장
a와 b의 값을 서로 바꾸고, 다시 a와 b를 나눔 - 나머지 나누기 b를 하기 위함
나머지가 0될 때까지 반복 - 나머지가 0이 되면 마지막으로 나누게 된 나머지가 최대공약수


"""