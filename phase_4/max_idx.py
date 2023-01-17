import sys
arr =[]
max = 0
for i in range(9):
    arr.append(int(sys.stdin.readline()))
    if arr[i] >max:
        max = arr[i]
        idx = i+1
print(f"{max}\n{idx}")