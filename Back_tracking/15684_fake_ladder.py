import sys
input = sys.stdin.readline

def backtracking(i, j, H, start):
    if i == H:
        return
    if not 0<= j < N:
        return
    if ladder[i][j]:
        if j < N:
            backtracking(i, j+1,H, start)
    


N, M, H = map(int, input().split())
if not M:
    print(0)
elif M == H*(N-1)/2:
    print(-1)
else:
    ladder = [[0] * N for _ in range(H)]
    for _ in range(M):
        x, y = map(int, input().split())
        ladder[y-1][x-1] = 1
    [print(*ladder[_]) for _ in range(H)]