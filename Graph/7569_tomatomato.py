import sys

input = sys.stdin.readline

move = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]

M, N, H = map(int, input().strip().split())

box = [[list(map(int, input().strip().split())) for _ in range(N)] for _ in range(H)]

# print(box)
