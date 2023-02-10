import sys

def permutation(arr, n, m):
    if len(arr) == m:
        print(*arr)
        return
    else:
        for i in range(1, n+1):
            if i not in arr:
                arr.append(i)               # i를 넣고
                permutation(arr, n, m)      # 재귀를 돌려서 i로시작하는 m개의 숫자 배열 출력
                arr.pop()                   # i 빼서 초기화

N, M = map(int, sys.stdin.readline().strip().split())
lst = []
permutation(lst, N, M)
