h,m = map(int, input().split())
if 45<=m<60:
    minute = m-45
    hour = h
elif m<45:
    minute = m+15
    if h>0:
        hour = h-1
    elif h==0:
        hour = 23
print(hour, minute)