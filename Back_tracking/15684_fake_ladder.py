# 15684 사다리 조작
import sys
input = sys.stdin.readline


def check_ladder() -> bool:
    for i in range(N):
        y, x = 0, i
        while y < H:
            if ladders[y][x] == 1:
                x -= 1
            elif ladders[y][x] == 2:
                x += 1
            y += 1
        if x != i:
            return 0
    return 1


def bt(cnt:int, start_i:int) -> None:
    global ans
    
    if check_ladder():
        ans = min(cnt, ans)
        return
    if cnt == 3:
        return 
    if cnt >= ans:
        return
    for i in range(start_i, H):
        for j in range(N-1):
            if not ladders[i][j] and not ladders[i][j+1]:
                ladders[i][j] = 2
                ladders[i][j+1] = 1
                bt(cnt+1, i)
                ladders[i][j] = 0
                ladders[i][j+1] = 0
    return


if __name__ == "__main__":
    N, M, H = map(int, input().split())
    ladders = [[0] * N for _ in range(H)]
    visited = [[0] * N for _ in range(H)]
    for _ in range(M):
        # 1 -> 왼쪽, 2 -> 오른쪽
        a, b = map(int, input().split())
        ladders[a-1][b-1] = 2
        ladders[a-1][b] = 1
    ans = 5
    bt(0,0)
    print(-1 if ans > 3 else ans)
        