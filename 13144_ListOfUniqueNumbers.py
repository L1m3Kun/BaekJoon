# 13144 List of Unique Numbers

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().strip().split()))

number = [0] * (N+1)
for i in range(1, N+1):
    number[i] = number[i-1] + 1

left = right = ans = 0
while left < N:
    if len(set(arr[left:right+1])) == (right - left +1):
        right += 1
    else:
        ans += number[right-left]
        left += 1 
print(ans)
    
        






# import sys
# input = sys.stdin.readline

# N = int(input())
# arr = list(map(int, input().split()))

# left = right = ans = 0

# while left < N:
#     if len(set(arr[left:right+1])) == (right-left+1):
#         right += 1
#     else:
#         left += 1

# if left:
#     if left == right -1:
#         print(N)
#     pass
# else:
    


'''실패작'''
# import sys
# input = sys.stdin.readline
# left = right = 0
    
# N = int(input())
# arr = list(map(int,input().split()))
# num = [0] * (N+1)
# for i in range(1,N+1):
#     num[i] = num[i-1]+i
# ans = 0
# # print(ans)
# while right < N:
#     print(left, right)
#     if len(set(arr[left:right+1])) == (right-left+1):
#         right += 1
#     else:
#         # for i in range(N-1, right-left-1, -1):
#         #     if ans[i]:
#         #         ans[i] -= 1
#         #     else:
#         #         break
#         # ans += num[right-left]
#         # print(ans)
#         ans += right -1
#         left += 1
#         # print(left)
#     # print(ans)
# # result = sum(ans)

# print(ans)
