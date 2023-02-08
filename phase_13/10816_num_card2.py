import sys
# 입력
N = int(sys.stdin.readline())
sang = {}
for m in list(map(int, sys.stdin.readline().strip().split())):
    # 딕셔너리로 저장
    if m not in sang.keys():
        sang[m] = 1
    else:
        sang[m] += 1
M = int(sys.stdin.readline())
# 입력을 key값으로 val가져오기
for q in list(map(int, sys.stdin.readline().strip().split())):
    if q in sang.keys():
        print(sang[q], end=" ")
    else:
        print(0, end=" ")


# 시간초과
# N = int(sys.stdin.readline())
# sang = list(map(int, sys.stdin.readline().strip().split()))
#
# M = int(sys.stdin.readline())

# for m in list(map(int, sys.stdin.readline().strip().split())):
#     cnt = 0
#     for n in sang:
#         if m == n:
#             cnt += 1
#     print(cnt, end=" ")
# for m in list(map(int, sys.stdin.readline().strip().split())):
#     print(sang.count(m), end=" ")