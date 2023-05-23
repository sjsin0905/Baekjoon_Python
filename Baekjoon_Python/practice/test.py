T = int(input())
min = {}
max = {}
yy_name = {}
mm_yy = {}
dd_mm = {}
y_list = []
for i in range(T):
    name, dd, mm, yy = input().split()
    dd, mm, yy = map(int, dd, mm, yy)
    yy_name[yy] = name
    mm_yy[mm] = yy
    dd_mm[dd] = mm
for j in yy_name.keys():
    y_list.append(j)
for q in range(1,T):
    if y_list[q-1] == y_list[q]:

y_list.sort()
min[y_list[0]] = yy_name.get(y_list[0])
y_list.sort(reverse=True)
max[y_list[0]] = yy_name.get(y_list[0])
