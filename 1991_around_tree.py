# 1991 트리 순회
import sys

input = sys.stdin.readline


def pre_order(N: int, tree: list, node: str) -> None:
    if node == ".":
        return
    print(node, end="")
    pre_order(N, tree, tree[node][0])
    pre_order(N, tree, tree[node][1])


def in_order(N: int, tree: list, node: str) -> None:
    if node == ".":
        return
    in_order(N, tree, tree[node][0])
    print(node, end="")
    in_order(N, tree, tree[node][1])


def post_order(N: int, tree: list, node: str) -> None:
    if node == ".":
        return
    post_order(N, tree, tree[node][0])
    post_order(N, tree, tree[node][1])
    if node != ".":
        print(node, end="")


def solution() -> None:
    N = int(input())
    tree = {}

    for _ in range(N):
        root, node1, node2 = input().strip().split()
        tree[root] = (node1, node2)
    pre_order(N, tree, "A")
    print()
    in_order(N, tree, "A")
    print()
    post_order(N, tree, "A")
    print()
    return


if __name__ == "__main__":
    solution()
