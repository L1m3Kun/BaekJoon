N, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=1)                     # 내림차순 정렬
print(arr[k-1])                         