import sys
from collections import deque

input = sys.stdin.readline

def check(arr):
    max_value = 0
    for i in range(H):
        for j in range(N):
            max_value = max(max_value, *visited[i][j])
            for k in range(M):
                if arr[i][j][k] == 0:
                    return 0
    return max_value


move = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]

M, N, H = map(int, input().strip().split())

box = [[list(map(int, input().strip().split())) for _ in range(N)] for _ in range(H)]

# print(box)
test = 0
queue = deque()
visited = [[[0] * M for _ in range(N)] for _ in range(H)]
for i in range(H):
    for j in range(N):
        for k in range(M):
            test += box[i][j][k]
            if box[i][j][k] == 1: 
                queue.append((i, j, k))
                visited[i][j][k] = 1
if test == -M*H*N or test == 0 or not queue:
    print(-1)
else:
    res = 0
    while queue:
        i, j, k = queue.popleft()
        box[i][j][k] = 1
        for di, dj, dk in move:
            ni = i + di
            nj = j + dj
            nk = k + dk
            if 0<=ni<H and 0<=nj<N and 0<=nk<M and visited[ni][nj][nk]==0 and box[ni][nj][nk]==0:
                queue.append((ni, nj, nk))
                visited[ni][nj][nk] = visited[i][j][k] + 1
    print(check(box)-1)
    