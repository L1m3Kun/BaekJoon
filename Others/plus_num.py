import sys

N = int(sys.stdin.readline().strip())
lst = sys.stdin.readline().strip()
lst = list(map(int,list(str(lst))))
sum = 0
for i in lst:
    sum += i
print(sum)