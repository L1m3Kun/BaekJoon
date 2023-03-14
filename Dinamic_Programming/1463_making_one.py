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
    for i in range(4, N+1):
        if not i % 3 and not i % 2: # 2와 3을 약수로 갖는 수
            dp[i-1] = 1 + min(dp[i-2], dp[(i-2)//3], dp[(i-2)//2])
        elif not i % 3: # 3을 약수로 갖는 수
            dp[i-1] = 1 + min(dp[i-2], dp[(i-2)//3])
        elif not i % 2: # 2를 약수로 갖는 수
            dp[i-1] = 1 + min(dp[i-2], dp[(i-2)//2])
        else: # 그 외
            dp[i-1] = 1 + dp[i-2]
    
print(dp[N-1])    