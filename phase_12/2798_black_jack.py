import sys
# 입력
N, M = map(int, sys.stdin.readline().strip().split())
arr = list(map(int, sys.stdin.readline().strip().split()))
# 값 초기화
sum_arr = max_sum = 0
# 3장을 뽑아 M을 넘지 않으면서 최대 합을 구하기
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            # 합 구하기
            sum_arr = arr[i] + arr[j] + arr[k]
            # M을 넘지 않으면서 최대 합 구하기
            if sum_arr <= M and max_sum < sum_arr:
                max_sum = sum_arr
print(max_sum)

