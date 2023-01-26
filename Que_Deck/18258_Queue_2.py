import sys


N = int(sys.stdin.readline())
que = []                            # queue 생성
for _ in range(N):
    order = list(sys.stdin.readline().strip().split())
    
    if order[0] == 'push':
        que.append(order[1])
    elif len(que) == 0:
        if order[0] == 'pop' or order[0] == 'size' or order[0] == 'front' or order[0] == 'back':
            print(-1)
        elif order[0] == 'empty':
            print(0)
    else:
        if order[0] == 'pop':
            print(que.pop(0))           # 첫번째 인자 빼기
        elif order[0] == 'size':
            print(len(que))
        elif order[0] == 'empty':
            print(1)
        elif order[0] == 'front':
            print(que[0])
        elif order[0] == 'back':
            print(que[-1])
    