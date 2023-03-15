import sys
input = sys.stdin.readline

s1 = '0'+input().strip()
s2 = '0'+input().strip()

dp = [0] * len(s1)
cnt = 1
for i in range(1,len(s2)):
    if s2[i] == s2[i-1]:
        cnt += 1
    else:
        cnt = 1
    tmp = cnt

    for j in range(1, len(s1)):
        if s2[i] == s1[j]:
            dp[j] = tmp+1
        else:
            tmp = max(tmp, dp[j])
    print(dp)
print(max(dp))