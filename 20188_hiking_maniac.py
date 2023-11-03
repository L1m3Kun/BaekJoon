# 20188 등산 마니아
import sys
from collections import deque

input = sys.stdin.readline


def to_top(N: int, graph: list, edge: dict, target: int):
    dp = [set([]) for _ in range(N + 1)]

    return


def solution(N: int, graph: list, edge: dict) -> None:
    return


if __name__ == "__main__":
    N = int(input())
    graph = [[] for _ in range(N + 1)]
    edge = {}
    for i in range(N - 1):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)
        edge[(s, e)] = i
        edge[(e, s)] = i
    solution(N, graph, edge)
