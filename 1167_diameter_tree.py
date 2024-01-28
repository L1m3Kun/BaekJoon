# 1167 트리의 지름
import sys
input = sys.stdin.readline


def prev(max_d:int,tree:list):
    visited


def solution():
    V = int(input())
    tree = [[0] * (V+1) for _ in range(V+1)]
    for _ in range(V):
        node = list(map(int, input().split()))
        for i in range(1, len(node)-1):
            if not i % 2:
                tree[node[0]][node[i-1]] = node[i]
    


if __name__ == "__main__":
    solution()