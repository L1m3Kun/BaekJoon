# 13144 List of Unique Numbers
import sys
input = sys.stdin.readline

# input
N = int(input())
arr = list(map(int, input().split()))

# setting
sequence = set()
# two pointer
left = right = 0
# answer
ans = 0

# 마지막까지 가면 끝
while right < N:
    if arr[right] not in sequence:   # sequence에 포함되어 있지 않으면
        sequence.add(arr[right])    # 추가
        right += 1                  # 다음칸으로
        ans += right-left           # 숫자를 더할 때 right-left+1 이므로 앞에서 미리 right += 1 하고 덧셈
    else:
        sequence.remove(arr[left])  # 있으면 그 숫자 빼고감
        left += 1                   

# output
print(ans)




'''실패작'''


# import sys
# input = sys.stdin.readline

# N = int(input())
# arr = list(map(int, input().strip().split()))

# number = [0] * (N+1)
# for i in range(1, N+1):
#     number[i] = number[i-1] + 1

# left = right = ans = 0
# while left < N:
#     if len(set(arr[left:right+1])) == (right - left +1):
#         right += 1
#     else:
#         ans += number[right-left]
#         left += 1 
# print(ans)
    
        






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
