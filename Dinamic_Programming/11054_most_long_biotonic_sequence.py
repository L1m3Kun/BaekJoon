import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
rev_arr = arr[::-1]     # 감소수열 용
inc = [1] * N       # 증가 수열 길이 구하기
dec = [1] * N       # 감소 수열 길이 구하기
for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:     # 증가
            inc[i] = max(inc[i], inc[j]+1)
        if rev_arr[i] > rev_arr[j]:     # 감소
            dec[i] = max(dec[i], dec[j]+1)
max_val = 0 # 최대값 구하기
for i in range(N):
    max_val = max(max_val,inc[i] + dec[N-1-i] -1)   # 자기자신 두번 들어가므로 -1

print(max_val)

