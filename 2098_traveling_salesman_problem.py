# 2098 외판원 순회
input = __import__("sys").stdin.readline


def dfs(now: int, digit: int, N: int, distance: list) -> int:
    global dp
    if digit == (1 << N) - 1:
        return


if __name__ == "__main__":
    N = int(input())
    distance = [list(map(int, input().split())) for _ in range(N)]
    dp = [[-1] * (1 << N) for _ in range(N)]
    print(dfs(N, distance))

"""
input = __import__("sys").stdin.readline
INF = int(1e9)

def dfs(now: int, digit_visited: int, N: int, distance: list) -> int:
    global dp
    if digit_visited == (1 << N) - 1:
        return distance[now][0] if distance[now][0] else INF

    if dp[now][digit_visited] == INF:
        return dp[now][digit_visited]

    for next in range(1, N):
        if not digit_visited & (1 << next) and distance[now][next]:
            dp[now][digit_visited] = min(
                dp[now][digit_visited],
                dfs(next, digit_visited | (1 << next), N, distance)
                + distance[now][next],
            )

    return dp[now][digit_visited]


if __name__ == "__main__":
    N = int(input())
    distance = [list(map(int, input().split())) for _ in range(N)]
    dp = [[-1] * (1 << N) for _ in range(N)]
    print(dfs(0, 1, N, distance))
"""

"""
input = __import__("sys").stdin.readline


def dfs(N: int,distance: list, minV: int) -> int:
    stack = [(0, 1, 0)]

    while stack:
        now, digit_visited, dist = stack.pop()
        if digit_visited == (1 << N) - 1:
            if distance[now][0]:
                minV = min(minV, dist + distance[now][0])
            continue
        for next in range(N):
            if not digit_visited & 1 << next and distance[now][next]:
                stack.append(
                    (next, digit_visited | 1 << next, dist + distance[now][next])
                )
    return minV


def solution(N: int, distance: list) -> int:
    minV = 1000000 * (N + 1)
    return dfs(N, distance, minV)


if __name__ == "__main__":
    N = int(input())
    distance = [list(map(int, input().split())) for _ in range(N)]
    print(solution(N, distance))


"""
