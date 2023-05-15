absent = [2, 5]
no_book = [7]

for student in range(1,11):
    if student in absent:
        continue
    elif student in no_book:
        print("{0},은 책이 없어서 혼나야겠다".format(student))
        break
    else:
        print("{0}, 책을 읽어보렴".format(student))