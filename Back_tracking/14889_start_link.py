import sys

def devide(start, end, ability):
    if start == end:
        # result.append(ability)
        # print(result)
        print(ability)
        return
    else:
        for j in range(end):
                if j not in stack:
                    stack.append(j)
                    print(stack)
                    devide(start+1, end, ability + arr[start][j]+arr[j][start])
                    stack.pop()
        return

N = int(sys.stdin.readline().strip())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
stack = []
result = []
abil = 0
devide(0,N//2, abil)
print(result)
# result.append(abs(devide(0,N//2) - devide(N//2, N)))
# print(min(result))

