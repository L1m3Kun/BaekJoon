# 23971 ZOAC 4
import sys, math

input = sys.stdin.readline


def solution():
    H, W, N, M = map(int, input().split())
    print(math.ceil(H / (N + 1)) * math.ceil(W / (M + 1)))


if __name__ == "__main__":
    solution()

"""
import sys

input = sys.stdin.readline


def check(i, j, H, W, N, M, room):
    if 0 <= i - N < H and 0 <= j - M < W and room[i - N][j - M]:
        return 0
    if 0 <= i - N < H and room[i - N][j]:
        return 0
    if 0 <= i - N < H and 0 <= j + M < W and room[i - N][j + M]:
        return 0
    if 0 <= j - M < W and room[i][j - M]:
        return 0
    if 0 <= j + M < W and room[i][j + M]:
        return 0
    if 0 <= i + N < H and 0 <= j - M < W and room[i + N][j - M]:
        return 0
    if 0 <= i + N < H and room[i + N][j]:
        return 0
    if 0 <= i + N < H and 0 <= j + M < W and room[i + N][j + M]:
        return 0

    return 1


def solution(H, W, N, M):
    room = [[0] * W for _ in range(H)]
    cnt = 0
    for i in range(H):
        for j in range(W):
            if check(i, j, H, W, N, M, room):
                room[i][j] = 1
                cnt += 1
    print


if __name__ == "__main__":
    H, W, N, M = map(int, input().split())
    solution(H, W, N, M)

"""
