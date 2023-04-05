import sys
input = sys.stdin.readline


def game_start(i, j):
    top = 1
    # bottom = 5
    for now in range(K):
        request = orders[now]
        di, dj = move[request]
        ni, nj = i+di, j+dj
        if 0<=ni<N and 0<=nj<M:
            if request == 1:
                pass
                tmp = row[0]
                for idx in range(2):
                    row[idx] = row[idx+1]
                row[2] = top
                bottom = check_field(ni,nj, row[1])
                col[1] = row[1]
            elif request == 2:
                pass
                tmp = row[2]
                for idx in range(2,0,-1):
                    row[idx] = row[idx-1]
                row[2] = top
                bottom = check_field(ni,nj, row[1])
                col[1] = row[1] = bottom
            elif request == 3:
                pass
                tmp = col[2]
                for idx in range(2,0,-1):
                    col[idx] = col[idx-1]
                col[0] = top
                bottom = check_field(ni,nj, col[1])
                row[1] = col[1]
            elif request == 4:
                pass
                tmp = col[0]
                for idx in range(2):
                    col[idx] = col[idx+1]
                col[2] = top
                bottom = check_field(ni,nj, col[1])
                row[1] = col[1]

            top = tmp
            i,j= ni, nj
            print('top=',top)
            print('row[1] =', row[1])
            dice[row[1]] = bottom
            print(dice[top])
    return

def check_field(x, y, k):
    bottom = dice[k]
    if bottom:
        field[x][y] = bottom
        return 0
    else:
        bottom = field[x][y]
        field[x][y] = 0
        return bottom

# 지도 세로: N, 지도 가로:M, 주사위 처음 위치(세로:x,가로:y)
N, M, x, y, K = map(int, input().split())
field = []
for _ in range(N):
    field.append(list(map(int, input().split())))
orders = list(map(int, input().split()))
#  1: 동쪽, 2: 서쪽, 3: 북쪽, 4: 남쪽
move = [(0,0), (0,1), (0,-1), (-1, 0), (1,0)]
dice = [0, 0, 0, 0, 0, 0, 0]
col = [2, 6, 5]
row = [4, 6, 3]
game_start(x, y)
