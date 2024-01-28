# 5052 전화번호 목록
import sys
input = sys.stdin.readline


def solution():
    n = int(input())
    contact_tree = {}
    for _ in range(n):
        phone = input().strip()
        for i in range(len(phone)):
            num = phone[i]
            if num not in contact_tree.keys():
                contact_tree[]
    return 


if __name__ == "__main__":
    for _ in range(int(input())):
        solution()