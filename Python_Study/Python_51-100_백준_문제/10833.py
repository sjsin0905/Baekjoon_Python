num = int(input())
sum = 0
for i in range(num):
    stu, apple = map(int, input().split())
    stu_na = apple // stu
    if stu > apple:
        sum += apple
    if stu_na > 0:
        sum += apple - (stu * stu_na)
print(sum)