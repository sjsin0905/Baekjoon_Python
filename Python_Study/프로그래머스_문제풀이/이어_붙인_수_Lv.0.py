def solution(num_list):
    even = []
    odd = []
    for i in range(len(num_list)):
        if num_list[i] % 2 == 0:
            even.append(num_list[i])
        else:
            odd.append(num_list[i])
    even_str = "".join(map(str, even))
    odd_str = "".join(map(str, odd))
    answer = int(even_str) + int(odd_str)
    return answer