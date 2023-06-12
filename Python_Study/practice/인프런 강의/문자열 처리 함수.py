python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python","Java"))

index = python.index("n")
print(index)

index = python.index("n",index +1) #2번째 n 찾기 (index 번째 이후 즉, 5번째 이후부터 다시 n찾기)
print(index)

print(python.find("Java")) #없는 문자 찾을시 -1 반환
# print(python.index("Java")) #없는 문자 찾을시 오류

print(python.count("n"))