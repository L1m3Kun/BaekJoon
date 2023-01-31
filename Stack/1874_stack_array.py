import sys

n = int(sys.stdin.readline())

stack_list = [int(sys.stdin.readline()) for _ in range(n)]
stack = [1]
result = ['+']
idx = 1
try:
    while len(stack_list) != 0:
        # stack 이 비었는가?
        if stack:
            # stack에 들어간 수와 입력이 같을 때
            if stack[-1] == stack_list[0]:
                result.append('-')
                stack.pop(-1)
                stack_list.pop(0)
            # stack에 들어간 수가 입력보다 작을 때
            elif stack[-1] < stack_list[0] or len(stack) == 0:
                for num in range(idx+1,stack_list[0]+1):
                    result.append('+')
                    stack.append(num)
                idx = stack_list[0]
            # 입력이 더 크면 에러 만들기
            else:
                raise ValueError()
                break
        #비었을 때 stack에 넣음
        else:
            for num in range(idx+1,stack_list[0]+1):
                result.append('+')
                stack.append(num)
            idx = stack_list[0]
    print('\n'.join(result))
except:
    print('NO')

    

