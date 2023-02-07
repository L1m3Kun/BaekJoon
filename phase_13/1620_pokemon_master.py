import sys

N, M = map(int, sys.stdin.readline().strip().split())
poke_dictionary = {i+1:sys.stdin.readline().strip() for i in range(N)}
quest = [sys.stdin.readline().strip() for _ in range(M)]

for idx in quest:
    if type(idx) == int:
        print(poke_dictionary[idx])
    elif type(idx) == str:
