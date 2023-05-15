# # , 부분에 넣을 양식 지정
# print("자바", "파이썬", "C++", sep =" vs ")
#
# # 끝에 양식 지정
# print("자바,파이썬", end = "?")
# print("무엇이 더 재밌을까요")
#

scores = {"수학": 0, "과학": 10, "영어": 100}
for subject, score in scores.items():
    # .ljust(8) 왼쪽으로 정렬 8칸 확보 / .rjust(4) 오른쪽으로 정렬 4칸 확보
    print(subject.ljust(8), str(score).rjust(4))


