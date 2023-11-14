# 16437 양 구출
from collections import defaultdict, deque

input = __import__("sys").stdin.readline


def bfs(tree: dict, nums: list, total: int) -> int:
    que = deque([(1, 0)])
    while que:
        now, sheeps = que.popleft()
        for next in tree[now]:
            if nums[next][0] == 1:
                tmp = sheeps + nums[next][1]
                if tmp > 0:
                    total += tmp
                    que.append((next, 0))
                else:
                    que.append((next, tmp))
            elif nums[next][0] == 0:
                que.append((next, sheeps - nums[next][1]))
    return total


def solution() -> int:
    N = int(input())
    tree = defaultdict(list)
    nums = [0] * (N + 1)
    for i in range(2, N + 1):
        is_sheep, num, bridge = input().strip().split()
        tree[int(bridge)].append(i)
        nums[i] = nums[i] + num if is_sheep else nums[i] - num

    return bfs(tree, nums, 0)


if __name__ == "__main__":
    print(solution())
