from random import *
count = 0
for customer in range(1, 51):
    time = randrange(5, 51)
    if 15 >= time >= 5:
        print("[O] {0}번쨰 손님 (소요시간: {1}분)".format(customer, time))
        count += 1
    else:
        print("[ ] {0}번째 손님 (소요시간: {1}분)".format(customer, time))

print("총 탑승 승객: {0}".format(count))
