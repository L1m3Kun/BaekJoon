import sys
n=[]
num=[]
arr=[0 for i in range(30)]
for i in range(28):
    n.append(int(sys.stdin.readline()))
    for j in range(30):
        if (j+1) == n[i]:
            arr[j] =1
for i in range(len(arr)):
    if arr[i] == 0:
        num.append(i+1)
if num[0]>num[1]:
    print(f'{num[1]}\n{num[0]}')
else:
    print(f'{num[0]}\n{num[1]}')