# weather = "비"
#
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 없음")

temp = int(input("기온 입력:"))
if 30 <= temp:
    print("hot")
elif 10 <= temp:
    print("good")
elif 0 <= temp:
    print("cold")
else:
    print("bad")