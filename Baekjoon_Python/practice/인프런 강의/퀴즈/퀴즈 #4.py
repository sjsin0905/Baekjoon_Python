from random import *

# 내가 쓴 답
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


shuffle(lst)
print(lst)
ck = sample(lst, 1)
print(ck)
del lst[lst.index(ck[0])]
coffe = sample(lst, 3)
print(" -- 당첨자 발표 -- ")
print("치킨 당첨자: " + str(ck))
print("커피 당첨자: " + str(coffe))
print(" -- 축하합니다 -- ")
print(lst[:])

# 강의 답안
# users = range(1, 21)
# users = list(users)
#
# shuffle(users)
#
# winner = sample(users, 4)
#
# print(" -- 당첨자 발표 -- ")
# print("치킨 당첨자: {0}".format(winner[0]))
# print("커피 당첨자: {0}".format(winner[1:]))
# print(" -- 축하합니다 -- ")

