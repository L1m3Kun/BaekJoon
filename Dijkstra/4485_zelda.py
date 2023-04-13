# 4485 녹색 옷 입은 애가 젤다지?
import sys
from collections import deque
import heapq
input = sys.stdin.readline

T = 0
dir = [(0,1),(0,-1),(1,0),(-1,0)]   # 젤ㄷ..아니 링크 방향
INF = 10 * 125*125
while True:
    T += 1 # test case
    N = int(input())
    if not N:   # N이 0이면 멈춰!
        break
    cave = [list(map(int, input().strip().split())) for _ in range(N)]  # 도둑놈들
    que = []
    heapq.heappush(que,(cave[0][0],0,0))
    visited = [[INF] * N for _ in range(N)]
    while que:
        w, i, j = heapq.heappop(que)
        for di, dj in dir:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N:
                if visited[ni][nj] > w+cave[ni][nj]:
                    heapq.heappush(que, (w+cave[ni][nj], ni, nj))
                    visited[ni][nj] = w+cave[ni][nj]


    print(f'Problem {T}: {visited[-1][-1]}')
# T = 0
# while True:
#     T += 1 # test case
#     N = int(input())
#     if not N:   # N이 0이면 멈춰!
#         break
#     cave = [list(map(int, input().strip().split())) for _ in range(N)]  # 도둑놈들
#     dir = [(0,1),(0,-1),(1,0),(-1,0)]   # 젤ㄷ..아니 링크 방향
#     que = deque([(0,0)])        # bfs용 queue
#     visited = [[0] * N for _ in range(N)]   
#     visited[0][0] = cave[0][0]+1    # 처음 시작이 0일 수도 있으니 처음에 1더해주고 마지막에 1뺌
#     while que:  #BFS 시작
#         i, j = que.popleft()
#         for di, dj in dir:
#             ni, nj = i+di, j+dj
#             if 0<=ni<N and 0<=nj<N: 
#                 if not visited[ni][nj]: # 처음 지나 가는 곳
#                     que.append((ni,nj))
#                     visited[ni][nj] = visited[i][j] + cave[ni][nj]
#                 elif visited[ni][nj] > visited[i][j] + cave[ni][nj]:        # 나중에 가도 가중치가 적은곳
#                     visited[ni][nj] = visited[i][j] + cave[ni][nj]
#                     que.append((ni,nj))
#     print(f'Problem {T}: {visited[-1][-1]-1}')
                

