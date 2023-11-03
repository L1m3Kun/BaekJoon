# 2292 벌집
import sys

input = sys.stdin.readline


def solution(N: int) -> None:
    """
    1           1개
    2 ~ 7       6개
    8 ~ 19      12개
    20 ~ 37     18개
    38 ~ 61     24개
    """
    start = distance = 1
    if N == 1:
        print(1)
        return
    while start <= 1000000000:
        if start < N <= start + distance * 6:
            print(distance + 1)
            break
        start += distance * 6
        distance += 1


if __name__ == "__main__":
    N = int(input())
    solution(N)
