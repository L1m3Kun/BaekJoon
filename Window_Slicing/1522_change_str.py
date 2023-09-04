# 1522 문자열 교환
import sys
from collections import deque

input = sys.stdin.readline

s = input().strip()
cnt = 0
# 초기 a 갯수 구하기
for i in s:
    if i == "a":
        cnt += 1
left, right = 0, cnt
# a를 한 곳으로 모으기 위해서는 갯수만큼 리스트 범위를 정함
# 정한 범위 내에서 b의 갯수가 바꾸는 수
# 초기 b의 개수가 minV 초기 값
b_count = 0
for b in s[left:right]:
    if b == "b":
        b_count += 1
minV = b_count
# 윈도우 슬라이싱을 통해 옮기는 횟수의 최소 구하기
while left < len(s):
    if s[left] == "b":
        b_count -= 1
    #  원형 큐 조심
    if s[right % len(s)] == "b":
        b_count += 1
    left += 1
    right = (right + 1) % len(s)
    minV = min(minV, b_count)
print(minV)
