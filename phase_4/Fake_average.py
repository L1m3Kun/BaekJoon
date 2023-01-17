import sys
n = int(sys.stdin.readline())
score = list(map(int, sys.stdin.readline().split()))
max=0
sum=0
for i in range(n):
    if score[i] >= max:
        max = score[i]
        idx = i
for i in range(n):
    score[i] = score[i]/max *100
    sum += score[i]
print(sum/n) 