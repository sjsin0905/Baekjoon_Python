while True:
    num = int(input())
    num_list = [1]
    if num == -1:
        break
    for i in range(2, num):
        if num % i == 0:
            num_list.append(i)
    sum = 0
    for k in num_list:
        sum += k
    num_list.remove(1)
    if sum == num:
        print(f"{num} = 1", end="")
        for j in num_list:
            print(" + " + str(j), end="")
        print("")
    else:
        print(f"{num} is NOT perfect.")
