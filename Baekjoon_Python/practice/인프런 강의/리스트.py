# 리스트[]

# 지하철 칸별로 10명, 20명, 30명

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호씨는 몇번째 칸에 타고있는가
print(subway.index("조세호"))

#하하씨가 다음 정류장에서 다음 칸에 탐
subway.append("하하")
print(subway)

subway.insert(1,"정형동")
print(subway)

# print(subway.pop())
# print(subway)

subway.append("유재석")
print(subway)
print(subway.count("유재석"))

num_list = [5,2,4,3,1]

num_list.sort()

print(num_list)

num_list.reverse()

print(num_list)

# num_list.clear()
# print(num_list)


mix_list = ["조세호", 20, True]

num_list.extend(mix_list)
print(num_list)
