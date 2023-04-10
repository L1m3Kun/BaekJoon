import sys
input = sys.stdin.readline


def game_start(i, j):
    top = 1 # 탑 초기값 설정
    for now in range(K):    # 모든 이동 요청에 대해
        request = orders[now]   # 요청방향 가져오기
        di, dj = move[request]  
        ni, nj = i+di, j+dj     # 방향에 따른 다음 위치
        if 0<=ni<N and 0<=nj<M: # 지도 안에서 움직일 때
            # 방향 = 1  
            if request == 1:
                # 오른쪽으로 가면 row가 왼쪽으로 회전
                # print('->')
                tmp = row[0]    # 탑으로 갈 idx
                for idx in range(2):    # 회전
                    row[idx] = row[idx+1]
                row[2] = top        # 위에 있던 아이가 빈 자리로 옴
                col[1] = row[1]     # bottom 값 조정
                check_field(ni,nj, row[1]) # 지도와 주사위 값 조정
            # 방향 = 2
            elif request == 2:
                # print('<-')
                # 왼쪽으로 가면 row가 오른쪽으로 회전
                pass
                tmp = row[2]
                for idx in range(2,0,-1):
                    row[idx] = row[idx-1]
                row[0] = top
                col[1] = row[1]
                check_field(ni,nj, row[1])
            # 방향 = 3
            elif request == 3:
                # print('A')
                # 위쪽으로 가면 col이 아래쪽으로 회전
                tmp = col[2]
                for idx in range(2,0,-1):
                    col[idx] = col[idx-1]
                col[0] = top
                row[1] = col[1]
                check_field(ni,nj, col[1])
            # 방향 = 4
            elif request == 4:
                # print('V')
                # 아래쪽으로 가면 col이 위쪽으로 회전
                tmp = col[0]
                for idx in range(2):
                    col[idx] = col[idx+1]
                col[2] = top
                row[1] = col[1]
                check_field(ni,nj, col[1])
            # top 값 조정
            top = tmp
            #  현재 위치 조정
            i,j= ni, nj
            #  주석을 풀고 돌려보시면 게임 진행이 나열됩니다.
            # dice[row[1]] = bottom
            # print('top=',top)
            # print('bottom =', row[1])
            # print('dice', dice)
            # print('dice idx')
            # print(*col, sep="\n")
            # print(*row)
            # print('field')
            # [print(field[a]) for a in range(N)]
            print(dice[top])
            # print('-------------')
    return

def check_field(x, y, bottom):
    tmp = field[x][y]   # 지도에 적힌 값
    if tmp: # 지도에 적힌 값이 0이 아니면
        field[x][y] = 0 # 지도에 적힌 값은 0이 되고
        dice[bottom] = tmp  # 주사위에 옮겨 붙음
    else:   # 지도에 적힌 값이 0이면
        field[x][y] = dice[bottom]      # 주사위에 있는 값 복사
    return
        
        

# 지도 세로: N, 지도 가로:M, 주사위 처음 위치(세로:x,가로:y)
N, M, x, y, K = map(int, input().split())
field = []
for _ in range(N):
    field.append(list(map(int, input().split())))
orders = list(map(int, input().split()))
#  1: 동쪽, 2: 서쪽, 3: 북쪽, 4: 남쪽
move = [(0,0), (0,1), (0,-1), (-1, 0), (1,0)]
# 주사위 값 저장
dice = [0, 0, 0, 0, 0, 0, 0]
# 주사위 index
#   2
# 4 1 3 
#   5
#   6
#  top은 따로 지정
col = [2, 6, 5] # 가로
row = [4, 6, 3] # 세로
game_start(x, y)    # 게임을 시작하지...
