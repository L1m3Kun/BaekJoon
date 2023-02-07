import sys
# set을 이용한 저장
N, M = map(int, sys.stdin.readline().strip().split())
S = set(sys.stdin.readline().strip() for _ in range(N))
M_list = [sys.stdin.readline().strip() for _ in range(M)]
# S에 M_list원소가 있으면 카운트
count = 0
for i in range(M):
    if M_list[i] in S:
        count += 1
print(count)
