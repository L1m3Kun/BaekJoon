import sys
# 0에서부터 수를 세기 시작하여 666이 들어가면 count += 1
# count == n 이되면 숫자세기를 그만두고 그 수를 출력
N = int(sys.stdin.readline())
end_num = 0
count = 0
while True:
    end_num += 1
    if '666' in str(end_num):
        count += 1
        if count == N:
            break
print(end_num)
