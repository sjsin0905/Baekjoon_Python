cabinet = {"A-3": "유재석", 100: "김태호"}
print(cabinet["A-3"])

print(cabinet.get(100))

# get으로 값 가져올때는 값이 없으면 none 표시 그냥 대괄호로 가져올때 값 없으면 프로그램 종료 오류 남

# 값 있는지 확인법
print("A-3" in cabinet)
print(5 in cabinet)

print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

del cabinet["A-3"]
print(cabinet)

print(cabinet.keys())

print(cabinet.values())

print(cabinet.items())

cabinet.clear()

print(cabinet)

