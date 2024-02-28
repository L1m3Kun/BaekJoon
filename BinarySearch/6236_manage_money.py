import sys
input = sys.stdin.readline


def check(mid:int, arr:list, N:int, M:int) -> int:
    K = mid
    cnt = 1
    for i in range(N):
        if cnt > M+2:
            return cnt
        if K >= arr[i]:
            K -= arr[i]
        else:
            if arr[i] > mid:
                return M + 1
            K = mid - arr[i]
            cnt += 1
    return cnt


def solution():
    N, M = map(int, input().split())
    arr = [int(input()) for _ in range(N)]
    s,e = min(arr), sum(arr)
    while s<=e:
        mid = (s+e)//2
        m = check(mid, arr, N, M)   
        if m == M:
            e = mid-1
            continue            
        elif m < M: 
            e = mid-1
        else:
            s = mid+1
    
    print(e+1)

if __name__ == "__main__":
    solution()
