import sys

def w(a,b,c):



while True:
    a,b,c = map(int, sys.stdin.readline().strip().split())
    if a == -1 and b == -1 and c == -1:
        break
    else:
        w(a,b,c)