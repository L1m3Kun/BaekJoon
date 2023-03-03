import sys
from collections import deque
input = sys.stdin.readline

direction = [(1,0), (0,1), (-1,0), (0,-1)]  # 방향

N, M = map(int, input().strip().split())
maze = [[0] * (M+2)] + [[0] + list(map(int,input().strip())) + [0] for _ in range(N)] +[[0] * (M+2)]
queue = deque([(1,1)])
visited = [[0]*(M+2) for _ in range(N+2)]       # 거리 계산용

visited[1][1] = 1   # 초기 설정
min_cnt = N*M       # 최단거리 저장
# BFS
while queue:
    i, j = queue.popleft()
    if i == N and j == M:               # 도착 시 최단거리만 저장
        if min_cnt > visited[i][j]:
            min_cnt = visited[i][j]
        continue
    elif visited[i][j] > min_cnt:       # 가다가 최소보다 커지면 다음꺼
        continue
    else:
        for di, dj in direction:
            ni = i + di
            nj = j + dj
            if maze[ni][nj] and not visited[ni][nj]:
                queue.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1

print(min_cnt)
# [print(*visited[i]) for i in range(N+2)]


# def DFS(arr,i,j, cnt):      # DFS
#     global min_cnt      # 최소값을 저장
#     if i == N and j == M:       # 도착 시 끝
#         min_cnt = min(min_cnt, cnt)
#         return
#     elif cnt >= min_cnt:     # 가다가 최소보다 커지면 거기까지만 탐색
#         return
#     else:
#         for di, dj in direction:        # 방향 다 찾기
#             ni = i + di
#             nj = j + dj
#             if maze[ni][nj]:
#                 arr[ni][nj] = 0        # 갈 수 있는 길이면 가보기
#                 DFS(arr, ni, nj, cnt+1)
#                 arr[ni][nj] = 1
#     return
# N, M = map(int, input().strip().split())
# maze = [[0] * (M+2)] + [[0] + list(map(int,input().strip())) + [0] for _ in range(N)] +[[0] * (M+2)]
#
# min_cnt = N*M           # 초기값은 최대로 돌았을때
# DFS(maze, 1, 1, 1)
# print(min_cnt)