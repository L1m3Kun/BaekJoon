import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().strip().split())

maze = [list(map(int, input())) for _ in range(N)]

queue = deque([(0,0,0)])

move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
while queue:
    i, j, b = queue.popleft()
    maze[i][j] = 1
    for di, dj in move:
        ni, nj = i + di, j + dj
        if 0<=ni<N and 0<=nj<M and not maze[ni][nj]:
            if b:
                queue.append((ni, nj, b))
            else:
                