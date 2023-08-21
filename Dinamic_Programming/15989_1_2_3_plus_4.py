# 15989 1, 2, 3 더하기 4
import sys

input = sys.stdin.readline
#  1로 만드는 방법 1가지를 디폴트
dp = [1] * 10001
dp[2] = 2
# 2의 배수일 때마다 2가 들어가는 경우의 수 추가
for i in range(3, 10001):
    dp[i] += dp[i - 2]
# 3의 배수일 때마다 3이 들어가는 경우의 수 추가
for i in range(3, 10001):
    dp[i] += dp[i - 3]

N = int(input())
for i in range(N):
    print(dp[int(input())])
