# 1515 수 이어 쓰기
import sys
from collections import deque

input = sys.stdin.readline
n = deque(list(input().strip()))

index = 0

while n:
    index += 1
    nums = deque(list(str(index)))
    while nums and n:
        # 처음 자리 수부터 확인
        if nums[0] == n[0]:
            # 만약 첫자리가 같다면 다음 자리수 확인을 위한 입력값에서 하나 빼기
            n.popleft()
        # 앞자리부터 빼면서 확인
        nums.popleft()
print(index)


# while n:
#     index += 1
#     nums = str(index)
#     while len(num) > 0 and len(n) > 0:
#         if num[0] == n[0]:
#             n = n[1:]
#         num = num[1:]
# print(index)
