# 2179 비슷한 단어
import sys

input = sys.stdin.readline

N = int(input())
words = []
maxIndex = [0, 0]
maxValue = 0
for k in range(N):
    word = input().strip()
    for s in range(len(words)):
        for i in range(min(len(word), len(words[s]))):
            if word[i] != words[s][i]:
                if maxValue < i:
                    maxValue = i
                    maxIndex = [s, k]
                elif maxValue == i:
                    if maxIndex[0] > s:
                        maxValue = i
                        maxIndex = [s, k]
                break
        else:
            if word != words[s]:
                if maxValue < min(len(word), len(words[s])):
                    maxValue = min(len(word), len(words[s]))
                    maxIndex = [s, k]
                elif maxValue == min(len(word), len(words[s])):
                    if maxIndex[0] > s:
                        maxValue = min(len(word), len(words[s]))
                        maxIndex = [s, k]

    words.append(word)
print(words[maxIndex[0]], words[maxIndex[1]], sep="\n")
