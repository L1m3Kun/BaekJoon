# 9465 sticker
import sys

input = sys.stdin.readline

"""
0 2 4 6 8
1 3 5 7 9

k번째 인덱스를 떼면
+1 +2 -2 를 못뗌
뗄수 있는곳 : 짝수 -1 -4 -3 홀수 -3 -4 -5

"""


def solution():
    for _ in range(int(input())):
        N = int(input())
        stickers = [0] * (N * 2)
        for i in range(2):
            arr = list(map(int, input().split()))
            for j in range(N):
                stickers[j * 2 + i] = arr[j]
        dp = [0] * (N * 2)
        dp[0] = stickers[0]
        dp[1] = stickers[1]
        for i in range(2, N * 2):
            # 홀수
            if i % 2:
                if 0 <= i - 3:
                    dp[i] = max(dp[i], dp[i - 3] + stickers[i])
                if 0 <= i - 4:
                    dp[i] = max(dp[i], dp[i - 4] + stickers[i])
                if 0 <= i - 5:
                    dp[i] = max(dp[i], dp[i - 5] + stickers[i])
            # 짝수
            else:
                if 0 <= i - 1:
                    dp[i] = max(dp[i], dp[i - 1] + stickers[i])
                if 0 <= i - 3:
                    dp[i] = max(dp[i], dp[i - 3] + stickers[i])
                if 0 <= i - 4:
                    dp[i] = max(dp[i], dp[i - 4] + stickers[i])
        print(max(dp[-1], dp[-2]))
    return


if __name__ == "__main__":
    solution()
