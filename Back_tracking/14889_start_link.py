import sys
input = sys.stdin.readline

def DFS(cnt, start):
    global ans
    if cnt == N//2:
        A = 0
        for i in range(N):
            for j in range(N):
                if stack[i] and stack[j]:
                    A += board[i][j]
                elif not stack[i] and not stack[j]:
                    A -= board[i][j]
        ans = min(ans, abs(A))
        return

    for u in range(start, N):
        if not stack[u]:
            stack[u] = 1
            DFS(cnt+1,u+1)
            stack[u] = 0

for test_case in range(1, int(input())+1):
    N = int(input())
    board = [list(map(int, input().strip().split())) for _ in range(N)]
    stack = [0]*N
    ans = 40000
    DFS(0,0)

    print(f'#{test_case} {ans}')
