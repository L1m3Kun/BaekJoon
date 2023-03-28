import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [[0,0]] + [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):     # 넣을 수 있는 물건의 수
    for j in range(1, K+1):     # 넣을 수 있는 무게의 가능성
        if j < arr[i][0]:           # 현재 쥐고있는 물건의 무게보다 작으면 이전의 값을 받으며 패스
            dp[i][j] = dp[i-1][j]
        else:                       # 현재 쥐고 있는 물건의 무게와 같거나 크면 쥐고있는 물건의 무게에서 제한된 K 까지 모든 경우의 수와 이전까지 저장된 값 비교
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-arr[i][0]]+ arr[i][1])
# [print(*dp[i]) for i in range(N+1)]
print(dp[N][K])













# dp = [[0]*2 for _ in range(101)]

# N, K = map(int, input().strip().split())
# arr  = [list(map(int, input().split())) for _ in range(N)]

# if N >= 1:
#     if arr[0][0] <= K:
#         dp[0][0], dp[0][1] = arr[0][0], arr[0][1] 
#     else: 
#         dp[0][0], dp[0][1] = 0, 0
# if N >= 2:
#     for i in range(1, N):
#         diff = K - arr[i][0]
#         if diff < 0:
#             dp[i][0], dp[i][1] = dp[i-1][0], dp[i-1][1]
#         else:
#             for j in range(i):
#                 # 현재 무게를 제외한 무게 중 가장 가치가 높은 경우를 찾기
#                 if diff >= dp[j][0]:
#                     # 현재 저장되어 있는 값과 비교해서 가치가 더 높은 경우 찾기
#                     if dp[i][1] < dp[j][1] + arr[i][1]:
#                         dp[i][0], dp[i][1] = dp[j][0]+arr[i][0], dp[j][1] + arr[i][1]
#                     # 만약 가치가 같다면 무게가 덜 나가는 것으로 넣기
#                     elif dp[i][1] == dp[j][1] + arr[i][1]:
#                         if dp[i][0] > dp[j][0] + arr[i][0]:
#                             dp[i][0], dp[i][1] = dp[j][0] + arr[i][0], dp[j][1] + arr[i][1]
#             if dp[i-1][1] > dp[i][1]:
#                 dp[i][0], dp[i][1] = dp[i-1][0], dp[i-1][1]
#             elif dp[i-1][1] == dp[i][1]:
#                 if dp[i-1][0] < dp[i][0]:
#                     dp[i][0], dp[i][1] = dp[i-1][0], dp[i-1][1]
# print(dp[:N])    


                        
                #     # 이전 값과 더 넣을 수 있는 무게 중 가치가 더 높은 것 넣기
                #     if dp[i-1][1] < dp[j][1] + arr[i][1]:
                #         # 현재 저장된 값과 비교하기
                #         if dp[i][1] < dp[j][1] + arr[i][1]:
                #             dp[i][0], dp[i][1] = dp[j][0]+arr[i][0], dp[j][1] + arr[i][1]
                #         elif dp[i][1] == dp[j][1] + arr[i][1]:
                #             if dp[i][0] > dp[j][0] + arr[i][0]:
                #                 dp[i][0], dp[i][1] = dp[j][0]+arr[i][0], dp[j][1] + arr[i][1]
                #     # 이전 값과 더 넣을 수 있는 무게가 같다면
                #     elif dp[i-1][1] == dp[j][1] + arr[i][1]:
                #         # 무게가 덜 나가는 것을 넣기
                #         if dp[i-1][0] < dp[j][0] + arr[i][0]:
                #             # 현재 저장된 값과 비교해서 넣기
                #             dp[i][0], dp[i][1] = dp[i-1][0], dp[i-1][1]
                #         else:
                #             dp[i][0], dp[i][1] = dp[j][0]+arr[i][0], dp[j][1] + arr[i][1]
                #     else:
                #         dp[i][0], dp[i][1] = dp[i-1][0], dp[i-1][1]
                # # 무게보다 작은 경우가 없을 땐 이전 값과 현재값 비교해서 넣기
                # else:
                #     if dp[i-1][1] > dp[i][1]:
                #         dp[i][0], dp[i][1] = dp[i-1][0], dp[i-1][1]
                #     elif dp[i-1][1] == dp[i][1]:
                #         if dp[i-1][0] < dp[i][0]:
                #             dp[i][0], dp[i][1] = dp[i-1][0], dp[i-1][1]

# print(dp[:N])

