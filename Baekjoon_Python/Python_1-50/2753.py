A = int(input())
if A % 4 == 0:
    if A % 100 != 0:
        print("1")
    elif A % 400 == 0:
        print("1")
    else:
        print("0")
else:
    print("0")

"""
다른사람 정답

a = int(input())
if (a%4==0 and a%100!=0) or a%400==0: print(1)
else: print(0)

"""