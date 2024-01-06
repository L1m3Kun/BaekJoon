# 1197 최소 스패닝 트리
import sys
input = sys.stdin.readline


def find(num: int) -> int:
    tmp = num
    while parent[tmp] != tmp:
        tmp = parent[tmp]
        parent[num] = tmp
    return parent[num]


def union(num1:int, num2:int) -> None:
    x = find(num1)
    y = find(num2)
    
    if x != y:
        parent[y] = x
    return


def kruskal(V:int, E:int, graph:list) -> int:
    node = []
    cost = 0
    for i in range(E):
        c, a, b = graph[i]
        if find(a) == find(b):
            continue
        node.append(i)
        union(a, b)
        cost += c
        if len(node) == V - 1:
            break
    return cost


if __name__ == "__main__":
    V, E = map(int, input().split())
    graph = []
    for _ in range(E):
        A, B, C = map(int, input().split())
        graph.append((C,A,B))
    graph.sort(key=lambda x:x[0])
    parent = [i for i in range(V+1)]
    print(kruskal(V, E, graph))