# 1의 개수 세기
import sys

input = sys.stdin.readline

A, B = map(int, input().split())

"""
2, 12 -> 2, 4
4자리
1이 1개인 경우
4가지
1이 2개인 경우

1이 3개인 경우


"""


def ten_to_bin(num):
    s = ""
    while num >= 1:
        if num == 1:
            s += "1"
            return s
        s += str(num % 2)
        num //= 2
    return s


binary_a = ten_to_bin(A)
binary_b = ten_to_bin(B)
