import sys

# def merge_sort(arr):
#     if len(arr) == 1:
#         return arr
#     else:
#         start = 0
#         end = len(arr)
#         mid = (start+end) //2
#         left = merge_sort(arr[start:mid])
#         right = merge_sort(arr[mid:end])
#
#         i = j = 0
#         tmp = []
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 tmp.append(left[i])
#                 i += 1
#             else:
#                 tmp.append(right[j])
#                 j += 1
#         if i == len(left):
#             tmp += right[j:]
#         if j == len(right):
#             tmp += left[i:]
#         return tmp


N = int(sys.stdin.readline())
arr = list((int(sys.stdin.readline().strip()), i) for i in range(N))
lst = []
arr2 = sorted(arr)
max_index = 0
for i in range(N):
    lst.append(arr2[i][1] - arr[i][1])
print(max(lst) +1)

# stack = []
# for _ in range(N):
#     i = int(sys.stdin.readline().strip())
#     if stack:
#         if i < stack[-1]:
#             stack.append(i)
#         else:
#             stack.pop()
#             stack.append(i)
#     else:
#         stack.append(i)
# print(len(stack)+1)