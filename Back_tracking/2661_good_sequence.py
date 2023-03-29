import sys
input = sys.stdin.readline

def back_tracking(string, N):
    global ans
    if len(string) >= 2:
        for j in range(1, len(string)//2+1):
            if string[len(string)-j:] == string[len(string)-2*j:len(string)-j]:
                return False
    if len(string) == N:
        ans = string
        return True
    for i in ['1', '2', '3']:
        if back_tracking(string+i, N):
            return True






def make_sequence(stack):
    global minV
    if len(stack) >= 2:
        for j in range(1, len(stack)//2+1):
            # print(stack[len(stack)-j:], stack[len(stack)-2*j:len(stack)-j])
            if stack[len(stack)-j:] == stack[len(stack)-2*j:len(stack)-j]:
                return     
    if len(stack) == N:
        # minV = min(minV, int(''.join(map(str,stack))))
        print(''.join(map(str, stack)))
        exit()
        # return
    for i in range(1, 4):
        stack.append(i)
        make_sequence(stack)
        stack.pop()
    return

N = int(input())
# stack = []
# minV = int('3' * N)
# make_sequence(stack)
# print(minV)
ans = ''
back_tracking('',N)
print(ans)