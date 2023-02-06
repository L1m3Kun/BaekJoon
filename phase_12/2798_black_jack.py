import sys

N, M = map(int, sys.stdin.readline().strip().split())
arr = list(map(int, sys.stdin.readline().strip().split()))

sum_arr = max_sum = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum_arr = arr[i] + arr[j] + arr[k]
            if sum_arr <= M and max_sum < sum_arr:
                max_sum = sum_arr
print(max_sum)

