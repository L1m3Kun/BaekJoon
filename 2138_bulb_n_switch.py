# 2138 전구와 스위치
import sys

input = sys.stdin.readline


def make_bulb_switch(N, start, end):
    set_list = set([])
    for i in range(N):
        if start[i] != end[i]:
            set_list.add(i)
    return set_list


def bitmasking(M):
    for i in range(1 << M):
        for j in range(M):
            if i & (1 << j):
                return


def solution():
    N = int(input())
    s_bulb = list(map(int, input().strip()))
    t_bulb = list(map(int, input().strip()))
    set_list = make_bulb_switch(N, s_bulb, t_bulb)

    return


if __name__ == "__main__":
    solution()


"""
import sys

input = sys.stdin.readline


def check(N, check_list, bulb, target):
    for i in range(N):
        if check_list[i] % 2:
            bulb[i] = 0 if bulb[i] else 1
    if bulb == target:
        return 1
    return 0


def switching(idx, N, bulb):
    for i in range(idx - 1, idx + 2):
        if 0 <= i < N:
            bulb[i] += 1
    return bulb


# def switching(N, bulb, index):
#     if index == 0:
#         arr = [0, 1]
#         # bulb[0], bulb[1] = map(lambda x: 0 if x else 1, [bulb[0], bulb[1]])
#     elif index == N - 1:
#         arr = [N - 2, N - 1]
#         # bulb[N - 1], bulb[N - 2] = map(
#         #     lambda x: 0 if x else 1, [bulb[N - 1], bulb[N - 2]]
#         # )
#     else:
#         arr = [index - 1, index, index + 1]
#         # bulb[index - 1], bulb[index], bulb[index + 1] = map(
#         #     lambda x: 0 if x else 1, [bulb[i] for i in range(index - 1, index + 2)]
#         # )
#     for i in arr:
#         bulb[i] = 0 if bulb[i] else 1
#     return bulb


def bitmasking(N, start_bulb, target):
    for i in range(1 << N):
        bulb = start_bulb.copy()
        check_list = [0] * N
        cnt = 0
        for j in range(N):
            if i & (1 << j):
                cnt += 1
                check_list = switching(j, N, check_list)
        if check(N, check_list, bulb, target):
            return cnt
    return 0


def solution():
    N = int(input())
    start_bulb = list(map(int, input().strip()))
    target_bulb = list(map(int, input().strip()))
    return bitmasking(N, start_bulb, target_bulb)


if __name__ == "__main__":
    print(solution())

"""
