'''
1. 0으로 표시된 위치 (x, y) 리스트에 저장
2. 첫 번째 빈칸에 1~9까지의 수 중 넣을 수 있는 수를 넣는다
    2-1. 빈칸의 행, 열. 3X3 확인
    2-2. 가능하면 빈칸에 그 수를 넣음
3. 다음 빈칸에 대해 2번 수행
4. 마지막 빈칸까지 채우면 스도쿠를 완성하므로 맵을 출력
'''

import sys

def check(x, y, k):
    for i in range(9):
        # 행에서 겹치는 수가 있는가?
        if board[y][i] == k:
            return 0
        # 열에서 겹치는 수가 있는가?
        if board[i][x] == k:
            return 0
    # 3x3 안에서 겹치는 수가 있는가?
    for i in range(3):
        for j in range(3):
            if board[((y//3)*3) + i][((x//3)*3) + j] == k:
                return 0
    return 1

def DFS(start):
    '''
    2. 첫 번째 빈칸에 1~9까지의 수 중 넣을 수 있는 수를 넣는다
    2-1. 빈칸의 행, 열. 3X3 확인
    2-2. 가능하면 빈칸에 그 수를 넣음
    3. 다음 빈칸에 대해 2번 수행
    '''
    if start == len(stack):
        # 4. 마지막 빈칸까지 채우면 스도쿠를 완성하므로 맵을 출력
        for k in range(9):
            print(*board[k])
        # 완성 후 프로그램 종료, 이거 안 하면 답이 여러개인 경우 계속 출력되어 '틀렸습니다' 나옵니다.
        exit(0)
        return
    else:
        y, x = stack[start]
        for i in range(1,10):
            if check(x,y,i):
                board[y][x] = i
                DFS(start+1)
                board[y][x] = 0
        return

stack = []
board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(9)]
# 1. 0으로 표시된 위치 (x, y) 리스트에 저장
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            stack.append((i,j))

# 2. 첫 번째 빈칸에 1~9까지의 수 중 넣을 수 있는 수를 넣는다
DFS(0)
# for k in range(9):
#     print(*board[k])

















# import sys
#
# def num_can(board):
#     for i in range(1,10):
#         num_check[i] = 9
#     for i in range(9):
#         for j in range(9):
#             if board[i][j] != 0:
#                 num_check[board[i][j]] -= 1
#     return num_check
#
#
# def check(start, j):
#     for i in range(start//3, 3):
#         for k in range(j//3, 3):
#             if (start,j) != (i,k) and board[start][j] == board[i][k]:
#                 return 1
#     return 0
#
#
# def sudoku(start):
#     if start == 9:
#         return
#     else:
#         for j in range(9):
#             if board[start][j] == 0:
#                 for k in range(9):
#                     board[start][j] = candidate[k]
#                     if check(start, j):
#                         continue
#                     for i in range(9):
#                         if j != i and (board[start][j] == board[start][i] or board[start][j] == board[i][start]):
#                             break
#                     else:
#                         sudoku(start+1)
#         return
#
# board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(9)]
# num_check = {}
# num_can(board)
# candidate = []
# for i in range(1, 10):
#     candidate += [i] * num_check[i]
# sudoku(0)
# print(board)