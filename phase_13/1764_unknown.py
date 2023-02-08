import sys
# set으로 문자열 받기
N, M = map(int, sys.stdin.readline().strip().split())
no_seen = set(sys.stdin.readline().strip() for _ in range(N))
no_heard = set(sys.stdin.readline().strip() for _ in range(M))
# 카운트세기 및 중복값 저장
cnt = 0
result = []
for s in no_seen:
    if s in no_heard:
       cnt += 1
       result.append(s)
#출력
print(cnt, *sorted(result), sep = "\n")
