import sys

N, M = map(int, sys.stdin.readline().strip().split())
rect = [list(sys.stdin.readline().strip()) for _ in range(N)]
chess1 = []
# 최대 색칠 수로 설정
min_paint = 64
# 비교할 체스판 만들기
for i in range(8):
    if i % 2:
        chess1.append(['B', 'W', 'B', 'W','B','W','B','W'])
    else:
        chess1.append(['W' ,'B', 'W', 'B', 'W','B','W','B'])
# 체스판과 비교하여 색칠할 곳 카운트
# 백으로 시작하는 체스판과 흑으로 시작하는 체스판을 동시에 비교
for i in range(N-7):
    for j in range(M-7):
        count_b = count_w = 0
        for k in range(8):
            for l in range(8):
                if rect[i+k][j+l] != chess1[k][l]:
                    count_b += 1
                else:
                    count_w += 1
        # 색칠 수의 최소 구하기
        if min_paint > count_b:
            min_paint = count_b
        if min_paint > count_w:
            min_paint = count_w
print(min_paint)