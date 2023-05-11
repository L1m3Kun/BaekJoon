# 1987 알파벳
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
board = [input().strip() for _ in range(R)]

que = [(0,0, board[0][0])]
# visited = board[0][0]
maxV = 0
max_len = set()
dir = [(0,-1), (0,1), (1,0), (-1,0)]
while que:
    i, j, visited = que.pop()
    # maxV = max(maxV, len(visited))
    
    # print(visited)
    for di, dj in dir:
        ni, nj = i+di, j+dj
        if 0<= ni <R and 0<=nj<C and board[ni][nj] not in visited:
            que.append((ni, nj, visited+board[ni][nj]))
            max_len.add(len(visited)+1)
print(max(max_len))

