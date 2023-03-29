import sys
input = sys.stdin.readline

def solution(n, k, arr):
    plug = [0] * n
    cnt = 0
    idx = 0
    if n == 1:
        for i in range(1, k):
            if arr[i] != arr[i-1]:
                cnt +=1
        return
    
    for i in range(k):
        if plug:
            if idx == n:
                if not arr[i] in plug:
                    plug[idx] = arr[i]
                    idx += 1
            else:
                cnt += 1
                for j in range(len(arr[i+1:])):
                    

                

        else:
            plug.append(arr[i])
    return

N, K = map(int, input().strip().split())
use = list(map(int, input().strip().split()))
