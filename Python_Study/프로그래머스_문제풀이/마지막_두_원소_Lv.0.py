def solution(num_list):
    size = len(num_list)-1
    if num_list[size-1] < num_list[size]:
        num_list.append(num_list[size] - num_list[size-1])
    else:
        num_list.append(num_list[size] * 2)
    return num_list