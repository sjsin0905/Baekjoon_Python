people = int(input())
cute = 0
not_cute = 0
for i in range(people):
    v = int(input())
    if v == 1:
        cute += 1
    elif v == 0:
        not_cute += 1
if cute > not_cute:
    print("Junhee is cute!")
elif not_cute > cute:
    print("Junhee is not cute!")
