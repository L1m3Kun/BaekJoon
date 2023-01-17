import sys
n=[]
for _ in range(28):
    n.append(int(sys.stdin.readline()))
n.sort()
print(n)
i=1
while i<=30:
    if i != n[i-1]:
        print(i)
        i+=2
    else:
        i+=1
    