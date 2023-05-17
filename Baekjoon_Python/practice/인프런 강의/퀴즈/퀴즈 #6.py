def std_weight(height, gender):
    height_m = int(height) / 100
    if gender == "남자":
        std = round(height_m * height_m * 22, 2)
        print("키 {0}cm {2}의 표준 체중은 {1}kg 입니다.".format(height, std, gender))
    elif gender == "여자":
        std = round(height_m * height_m * 21, 2)
        print("키 {0}cm {2}의 표준 체중은 {1}kg 입니다.".format(height, std, gender))
    else:
        gender = input("성별을 다시 입력하세요")
        std_weight(height, gender)

height = input("키를 입력하세요")
gender = input("성별을 입력하세요")
std_weight(height, gender)