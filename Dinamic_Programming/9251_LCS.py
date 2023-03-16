import sys
input = sys.stdin.readline

s1 = input().strip()
s2 = input().strip()

dp = [[0] * (len(s2)+1) for _ in range(len(s1)+1)]

for i in range(1, len(s2)):
    for j in range(1, len(s1)):
        if s2[i] == s1[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j-1])
[print(*dp[i]) for i in range(len(s2))]

print(dp[-1][-1])

# dp = [0] * 1000
# for i in range(len(s2)):
#     cnt = 0
#     for j in range(len(s1)):
#         if s2[i] == s1[j]:
#             dp[j] = max(cnt +1, dp[j]+1)
#         else:
#             cnt = max(cnt, dp[j])
# print(max(dp))