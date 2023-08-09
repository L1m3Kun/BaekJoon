# 20920 영단어 암기는 괴로워
import sys
from collections import defaultdict

input = sys.stdin.readline

N, M = map(int, input().split())

voca = defaultdict(int)

for _ in range(N):
    word = input().strip()
    if len(word) >= M:
        voca[word] += 1

vocaList = []
for key, val in voca.items():
    vocaList.append((-val, key))
vocaList.sort(key=lambda x: (x[0], -len(x[1]), x[1]))

for item in vocaList:
    print(item[1])
