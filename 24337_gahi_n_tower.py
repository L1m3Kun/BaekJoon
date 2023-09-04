# 24337 가희와 탑
import sys

input = sys.stdin.readline

"""
limits
1 <= N <= 100000
1 <= a <= N
1 <= b <= N
"""

# input
N, a, b = map(int, input().split())
answer = [0] * N
cnt = 1

if a > b:
    pass
elif a == b:
    pass
else:
    pass


# pivot = 0


# if a + b < N or (a + b == N and a == b):
#     if a == 1:
#         for i in range(N - (a + b) + 1, -1, -1):
#             answer[i] = cnt
#             cnt += 1
#         for i in range(N - (a + b) + 1, N):
#             answer[i] = 1
#         print(" ".join(map(str, answer)))
#     elif b == 1:
#         for i in range(N - (a + b) + 1, N):
#             answer[i] = cnt
#             cnt += 1
#         for i in range(N - (a + b) + 1):
#             answer[i] = 1
#         print(" ".join(map(str, answer)))
#     else:
#         if a > b:
#             for i in range(N - (a + b) + 1, N - b + 1):
#                 answer[i] = cnt
#                 cnt += 1
#             cnt = 1
#             for i in range(N - 1, N - b - 1, -1):
#                 if not answer[i]:
#                     answer[i] = cnt
#                     cnt += 1
#             for i in range(N - (a + b) + 1):
#                 answer[i] = 1
#             print(" ".join(map(str, answer)))
#         else:
#             for i in range(N - (a + b) + 1, N - b):
#                 answer[i] = cnt
#                 cnt += 1
#             cnt = 1
#             for i in range(N - 1, N - b - 1, -1):
#                 answer[i] = cnt
#                 cnt += 1
#             for i in range(N - (a + b) + 1):
#                 answer[i] = 1
#             print(" ".join(map(str, answer)))

# elif a + b == N:
#     answer[0] = answer[-1] = 1
#     for i in range(1, a + 1):
#         answer[i] = cnt
#         cnt += 1
#     cnt = 1
#     for i in range(N - 2, N - b - 2, -1):
#         answer[i] = cnt
#         cnt += 1
#     print(" ".join(map(str, answer)))

# else:
#     for i in range(a):
#         answer[i] = i + 1
#     for i in range(N - 1, N - b - 1, -1):
#         if answer[i]:
#             pivot += 1
#             if pivot >= 2:
#                 print(-1)
#                 break
#         answer[i] = max(cnt, answer[i])
#         cnt += 1
#     else:
#         print(" ".join(map(str, answer)))
