import sys

N = int(sys.stdin.readline().strip())
arr = [[0] * N for _ in range(N)]
for _ in range(N-1):
    x, y = map(int, sys.stdin.readline().strip().split())
    arr[x-1][y-1] = 1
    arr[y-1][x-1] = 1
par = [[] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            par[i].append(j)

print(arr)
print(par)


# import sys
# from collections import deque
#
# def DFS(start):
#     ans.append(start)
#     lst[start] = 1
#     if start == 0:
#         print(ans.popleft()+1)
#         return
#     for j in range(N):
#         if arr[j][start] == 1 and lst[j] == 0:
#             DFS(j)
#             lst[j] = 0
#     return
#
#
#
# N = int(sys.stdin.readline().strip())
# arr = [[0] * N for _ in range(N)]
# for _ in range(N-1):
#     x, y = map(int, sys.stdin.readline().strip().split())
#     arr[x-1][y-1] = 1
#     arr[y-1][x-1] = 1
# que = deque()
# for i in range(1, N):
#     for j in range(N):
#         if arr[j][i] == 1:
#             que.append(j)
#     if len(que) == 1:
#         print(que.popleft()+1)
#     else:
#         while que:
#             lst = [0] * N
#             lst[i] = 1
#             t =que.popleft()
#             ans = deque()
#             DFS(t)
