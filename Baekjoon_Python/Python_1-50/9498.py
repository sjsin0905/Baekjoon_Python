score = int(input())

if 90 <= score <= 100:
    grade = "A"
    print(grade)
elif 80 <= score < 90:
    grade = "B"
    print(grade)
elif 70 <= score < 80:
    grade = "C"
    print(grade)
elif 60 <= score < 70:
    grade = "D"
    print(grade)
else:
    grade = "F"
    print(grade)
