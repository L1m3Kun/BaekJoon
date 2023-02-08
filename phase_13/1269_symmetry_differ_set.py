import sys


N, M = map(int, sys.stdin.readline().strip().split())
A = set(map(int, sys.stdin.readline().strip().split()))
# 입력 내에서 중복값은 빼고 중복되지 않은 값은 더해줌
for i in set(map(int, sys.stdin.readline().strip().split())):
    if i not in A:
        A.add(i)
    else:
        A.discard(i)
print(len(A))

# 새로운 set에 넣는 형식, 위가 시간이 더 짧음 100ms 정도
# result = set()
# for i in A:
#     if i not in B:
#         result.add(i)
# for i in B:
#     if i not in A:
#         result.add(i)
#
# print(len(result))
