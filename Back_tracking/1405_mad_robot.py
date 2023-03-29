import sys
input = sys.stdin.readline

n, E, W, S, N = map(int, input().strip().split())
if E == S == 0 or W == N == 0 or W == S == 0 or E == N == 0:
    print(1.0)
else:
    pass