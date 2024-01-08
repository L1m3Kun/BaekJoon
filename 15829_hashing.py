# 15829 Hashing
import sys
input = sys.stdin.readline


def hashing(L:int, S:str) -> int:
    hash = 0
    for i in range(L):
        hash += (ord(S[i])-96)*(31**i)
    return hash%1234567891

if __name__ == "__main__":
    L = int(input())
    S = input().strip()
    ans = hashing(L,S)
    print(ans)