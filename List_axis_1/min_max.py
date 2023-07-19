import sys
n=int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
max = -1000000
min = 1000000
for i in arr:
    if i >= max:
        max = i
    if i <= min:
        min = i
print(f'{min} {max}')