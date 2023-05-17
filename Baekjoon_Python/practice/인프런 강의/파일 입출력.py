score_file = open("score.txt", "w", encoding="utf8")
print("수학: 0", file=score_file)
print("과학: 100", file=score_file)
print("영어: 90", file=score_file)
score_file.close()


# w = 덮어쓰기, a = 이어쓰기, r = 읽기

score_file = open("score.txt", "r", encoding="utf8")
# 전부 다 읽기
#print(score_file.read())

# 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")

score_file.close()

"""
몇 줄인지 모를때 계속 한 줄 씩 끝날때 까지 가져오기

score_file = open("score.txt", "r", encoding="utf8")
while Ture:
    line = score.file.readline()
    if not line:
        break
    print(line)
score_file.close()


"""


"""

리스트로 가져와서 읽기

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()     리스트 형태로 저장
for line in lines:
    print(line, end="")
    
score_file.close()


"""
