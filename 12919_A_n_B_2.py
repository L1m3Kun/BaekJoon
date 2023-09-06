# 12919 A와 B 2
import sys

input = sys.stdin.readline

S = input().strip()
T = input().strip()


def addA(s):
    s += "A"


def addB(s):
    s += "B"
    tmp = ""
    for s in range(len(s) - 1, -1, -1):
        tmp += s
    s = tmp


def bfs(s):
    if len(s) == len(T):
        if s == T:
            return 1
        return
    addA(s)

    addB(s)
