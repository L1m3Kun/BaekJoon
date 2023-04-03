import sys
from collections import deque
input = sys.stdin.readline



def game_start(i, cnt, val):
    global max_kda
    
    if cnt == 3:
        max_kda = max(max_kda, val)
        return
    if i == M:
        return

    tmp = [[0] *M for _ in range(N)]
    for k in range(N):
        tmp[k] = field[k].copy()
    game_start(i+1, cnt + 1, val + score(i))
    for k in range(N):
        field[k] = tmp[k].copy()
    game_start(i+1, cnt, val)
    return




def score(place):
    kda = 0
    # arr = [[0]*N for _ in range(M)]
    # for i in range(N):
    #     for j in range(M):
    #         arr[i][j] = field[i][j]
    for i in range(N-1, -1, -1):
        kda += one_archer_kill(i, place)
    return kda


def one_archer_kill(stage, place):
    

N, M, D = map(int, input().strip().split())
field = [list(map(int, input().strip().split())) for _ in range(N)]
max_kda = 0
game_start(0, 0, 0)
print(max_kda)

