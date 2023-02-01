import sys

# Bubble sort는 한계인가..?
# def bubble_sort(arr, N, k):
#     for last in range(N-1, k, -1):
#         for idx in range(last):
#             if arr[idx] > arr[idx+1]:
#                 arr[idx], arr[idx+1] = arr[idx+1], arr[idx]
#     return arr


N, k = map(int, sys.stdin.readline().strip().split())
arr = list(map(int, sys.stdin.readline().strip().split()))
# arr.sort()
print(bubble_sort(arr, N, k)[k-1])
# print(arr[k-1])