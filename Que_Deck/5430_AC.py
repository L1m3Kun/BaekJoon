import sys
from collections import deque
for test_case in range(1, int(sys.stdin.readline().strip())+1):
    order = sys.stdin.readline().strip()
    n = int(sys.stdin.readline().strip())
    # arr = list(ys.stdin.readline().strip('[').strip().strip(']').split(','))
    arr = deque(sys.stdin.readline().strip('[]\n').split(','))

    pointer = 0
    for i in order:
        # 회전
        if i == 'R':
            # 포인터 반전
            pointer = not pointer
        elif i == 'D':
            # 내용이 없으면 error
            # if arr == [""] or not arr:
            if arr == deque([""]) or not arr:
                print('error')
                break
            # 포인터 위치에서 빼기
            if pointer:
                arr.pop()
            else:
                # arr.pop(0)
                arr.popleft()
    else:
        if pointer:
            arr.reverse()
        print('[' + ','.join(arr) + ']')

