import sys

N, M = map(int, sys.stdin.readline().strip().split())
rect = [list(sys.stdin.readline().strip()) for _ in range(N)]
chess1 = []
min_paint = 64
for i in range(8):
    if i % 2:
        chess1.append(['B', 'W', 'B', 'W','B','W','B','W'])
    else:
        chess1.append(['W' ,'B', 'W', 'B', 'W','B','W','B'])
for i in range(N-7):
    for j in range(M-7):
        count_b = count_w = 0
        for k in range(8):
            for l in range(8):
                if rect[i+k][j+l] != chess1[k][l]:
                    count_b += 1
                else:
                    count_w += 1
        if min_paint > count_b:
            min_paint = count_b
        if min_paint > count_w:
            min_paint = count_w
print(min_paint)