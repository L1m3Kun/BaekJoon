def d(n):
    num = n
    for i in range(len(list(str(n)))):
        num += int(list(str(n))[i])
    return num
# 출력 리스트 생성
arr = list(range(1,10001))
# 중복 제거
for i in range(1, 10001):
    if d(i) in arr:
        arr.remove(d(i))
#출력
for num in arr:
    print(num)