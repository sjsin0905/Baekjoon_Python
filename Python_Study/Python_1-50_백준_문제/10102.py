people = int(input())
v = input()
count_A = 0
count_B = 0
for i in range(people):
    if v[i] == "A":
        count_A += 1
    elif v[i] == "B":
        count_B += 1

if count_A > count_B:
    print("A")
elif count_B > count_A:
    print("B")
else:
    print("Tie")