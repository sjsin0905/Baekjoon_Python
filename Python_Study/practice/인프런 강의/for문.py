# for waiting_no in range(1, 6):
#     print("대기번호 : {0}".format(waiting_no))

star = ["아이언맨", "토르", "그루트"]
for customer in star:
    print("손님: {0}".format(customer))


# 한줄 for문

student = ["aaaa", "bbbbbbbb", "cccccccccc"]
student = [len(i) for i in student]
print(student)