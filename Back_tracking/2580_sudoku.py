import sys

def check(start, i, j):


    return

def sudoku(start):
    if start == 9:
        return
    else:
        for i in range(9):
            for j in range(9):
                if board[start][i] == 0:
                    board[start][i] = j
                    if check(start, i, j):
                        sudoku(start+1)
                        board[start][i] = 0

board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(9)]
