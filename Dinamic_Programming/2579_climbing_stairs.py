import sys
input = sys.stdin.readline

N = int(input())
stairs = [int(input()) for _ in range(N)]
# print(stairs)
dp = [0] * 301
if N >= 1:      # 한 칸일 때 저장, 한칸 이상이어도 필요하므로 저장
    dp[0] = stairs[0]
if N >= 2:      # 두 칸일 때 저장, 두칸 이상이어도 필요하므로 저장
    dp[1] = stairs[1] + stairs[0]
if N >= 3:      # 세 칸일 때 저장, 세칸 이상이어도 필요하므로 저장
    dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])
if N >= 4:      # 네 칸 이상일 때 for문을 통해 이전 최대값을 이용한다.
    for i in range(4, N+1):
        dp[i-1] = stairs[i-1] + max(dp[i-3], dp[i-4]+stairs[i-2])
print(dp[N-1])