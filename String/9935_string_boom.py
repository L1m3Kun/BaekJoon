import sys

s = sys.stdin.readline().strip()
boom = sys.stdin.readline().strip()

stack = []
for i in range(len(s)):
    stack.append(s[i])
    if i >= len(boom)-1 and stack[-1] == boom[-1]:
        j = 1
        while True:
            if stack[-j] == boom[-j] and j == len(boom):
                [stack.pop() for _ in range(j)]
                break
            elif stack[-j] == boom[-j]:
                j += 1
                continue
            else:
                break
if stack:
    print(''.join(stack))
else:
    print('FRULA')



