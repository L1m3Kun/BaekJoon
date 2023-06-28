import sys
from collections import deque
input = sys.stdin.readline

dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def find_j_f():
    for i in range(R):
        for j in range(C):
            if maze[i][j] == "J":
                start.append(i)
                start.append(j)
            elif maze[i][j] == "F":
                fire.append((i, j))


def bfs(start_y, start_x):
    que = deque([(start_y, start_x, 0)])
    visited_jihoon = [[0]*C for _ in range(R)]
    visited_fire = [[0]*C for _ in range(R)]
    for idx in range(len(fire)):
        que.append((fire[idx][0], fire[idx][1], 1))
        visited_fire[fire[idx][0]][fire[idx][1]] = 1
    visited_jihoon[start_y][start_x] = 1
    while que:
        i, j, is_fire = que.popleft()
        for di, dj in dir:
            ni, nj = i+di, j+dj
            if is_fire:
                if 0<=ni<R and 0<=nj<C and (not visited_fire[ni][nj] or visited_fire[ni][nj] < visited_fire[i][j]):
                    visited_fire[ni][nj] = visited_fire[i][j]+1
                    que.append((ni,nj,1))
            else:
                if ni < 0 or ni >= R or nj < 0 or nj >= C:
                    return visited_jihoon[i][j]
                elif maze[ni][nj] == "." and (visited_jihoon[i][j]<visited_fire[ni][nj] or not visited_fire[ni][nj]):
                    visited_jihoon[ni][nj] = visited_jihoon[i][j] + 1
                    que.append((ni,nj,0))
    return "IMPOSSIBLE"

R, C = map(int, input().strip().split())
maze = [input().strip() for _ in range(R)]
fire = []
start = []
find_j_f()
print(bfs(start[0], start[1]))

