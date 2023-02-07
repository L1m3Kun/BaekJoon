import sys
# 입력
num = int(sys.stdin.readline())
# 각 자리수 합 + 원래 값 = 입력값 인 원래 값 출력
for i in range(num):
    if num == (i +sum(list(map(int, list(str(i)))))):
        print(i)
        break
else:
    # 없으면 0을 출력
    print(0)