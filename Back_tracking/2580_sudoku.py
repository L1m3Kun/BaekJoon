import sys

def num_can(board):
    for i in range(1,10):
        num_check[i] = 9
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                num_check[board[i][j]] -= 1
    return num_check


def check(start, j):
    for i in range(start//3, 3):
        for k in range(j//3, 3):
            if (start,j) != (i,k) and board[start][j] == board[i][k]:
                return 1
    return 0


def sudoku(start):
    if start == 9:
        return
    else:
        for j in range(9):
            if board[start][j] == 0:
                for k in range(9):
                    board[start][j] = candidate[k]
                    if check(start, j):
                        continue
                    for i in range(9):
                        if j != i and (board[start][j] == board[start][i] or board[start][j] == board[i][start]):
                            break
                    else:
                        sudoku(start+1)
        return

board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(9)]
num_check = {}
num_can(board)
candidate = []
for i in range(1, 10):
    candidate += [i] * num_check[i]
sudoku(0)
print(board)