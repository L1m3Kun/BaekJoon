import sys
input = sys.stdin.readline

dp = [[0]*101 for _ in range(2)]

N, K = map(int, input().strip().split())
arr  = [list(map(int, input().split())) for _ in range(N)]
if arr[0][0] <= K:
    dp[0][0] = arr[0][0]
    dp[0][1] = arr[0][1]
else:
    dp[0][0] = 0
    dp[0][1] = 0
for i in range(1, N):
    w, v = map(int, input().strip().split())
    for j in range(i):
