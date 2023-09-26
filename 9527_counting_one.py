# 1의 개수 세기
import sys

input = sys.stdin.readline

A, B = map(int, input().split())

"""
1 -> 1
2 -> 3     4
3 -> 8     12
4 -> 20    32
5 -> 

"""

square = [0] * 60
num = 1
b = max(A, B)
a = min(A, B)
