import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * (10**6+1)
if N >= 1:
    dp[0] = 0
if N >= 2:
    dp[1] = 1
if N >= 3:
    dp[2] = 1
if N >= 4:
    cnt = 0
    while N > 1:
        cnt += 1
        if not N % 3:
            N //= 3
        elif not N % 2:
            N //= 2
        else:
            N -= 1
        if N == 1:
            dp[N-1] = cnt
            break
print(dp[N-1])    