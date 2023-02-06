import sys
num = int(sys.stdin.readline())

for i in range(num):
    if num == (i +sum(list(map(int, list(str(i)))))):
        print(i)
        break
else:
    print(0)