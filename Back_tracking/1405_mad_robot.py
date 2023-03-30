import sys
input = sys.stdin.readline

def backtracking(cnt,i, j, percent):
    global ans
    if cnt == n:
        return
    for k in go:
        di, dj = dir[k]
        ni, nj = i + di, j + dj
        if not visited[ni][nj]:
            visited[ni][nj] = 1
            backtracking(cnt+1,ni, nj, percent*per[k] * 0.01)
            visited[ni][nj] = 0
        else:
            ans += percent * per[k] * 0.01
    

dir = [(0,1), (0,-1), (-1,0), (1,0)]
n, *per = map(int, input().strip().split())
if per[0] == per[2] == 0 or per[1] == per[3] == 0 or per[1] == per[2] == 0 or per[0] == per[3] == 0:
    print(1.0)
elif n == 1:
    print(1.0)
else:
    visited = [[0] * (2*n+1) for _ in range(2*n+1)]
    visited[n][n] = 1
    go = []
    ans = 0
    for i in range(4):
        if per[i] != 0:
            go.append(i)
    backtracking(0, n, n, 1)

    print(1-ans)