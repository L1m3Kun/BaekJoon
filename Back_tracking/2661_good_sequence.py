import sys
input = sys.stdin.readline

def make_sequence(stack):
    global minV
    if len(stack) >= 2:
        for j in range(1, len(stack)//2+1):
            # print(stack[len(stack)-j:], stack[len(stack)-2*j:len(stack)-j])
            if stack[len(stack)-j:] == stack[len(stack)-2*j:len(stack)-j]:
                return     
    if len(stack) == N:
        minV = min(minV, int(''.join(map(str,stack))))
        return
    for i in range(1, 4):
        stack.append(i)
        make_sequence(stack)
        stack.pop()
    return

N = int(input())
stack = []
minV = int('3' * N)
make_sequence(stack)
print(minV)
