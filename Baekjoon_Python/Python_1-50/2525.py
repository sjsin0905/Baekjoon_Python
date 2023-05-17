hour, min = input().split(" ")
use_time = int(input())

hour = int(hour)
min = int(min)

if use_time >= 60:
    use_time_h = use_time // 60
    use_time_m = use_time - (use_time_h * 60)
else:
    use_time_h = 0
    use_time_m = use_time

if use_time_m + min >= 60:
    result_time_m = use_time_m + min - 60
    use_time_h += 1
else:
    result_time_m = use_time_m + min

if use_time_h + hour >= 24:
    result_time_h = use_time_h + hour - 24
else:
    result_time_h = use_time_h + hour

print(f"{result_time_h} {result_time_m}")