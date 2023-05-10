import sys
input = sys.stdin.readline


N = int(input().strip())
queue = [-1]+[0] * 100001
root = 1
last = 1        # 마지막 값이 들어가 있는 숫자
ans = []        # 정답 리스트

def addHeap(n):
    global root, last
    if not queue[root]:     # 아무것도 없으면 그냥 넣어
        queue[root] = n
    else:                   # 무언가 있으면 마지막에 넣고 부모와 비교
        last += 1
        queue[last] = n
        idx = last
        while idx//2 >0:
            if queue[idx] < queue[idx//2]:
                queue[idx], queue[idx//2] = queue[idx//2], queue[idx]
            else:   # 비교했는데 부모가 나보다 작으면 그만
                break
            idx //= 2
        

def popHeap():
    global root, last
    if not queue[root]: # 아무것도 없는데 빼려하면 0
        ans.append(0)
        return 0
    ans.append(queue[root])
    # res = queue[root]
    queue[root] = queue[last]   # 마지막 값을 루트로 가져옴(루트 제거)
    queue[last] = 0 # 마지막 값 제거
    if last > 1:    # 마지막 인덱스는 1보다 작을 수 없음
        last -= 1
    idx = root  # 인덱스에서 시작
    while True:
        # 인덱스가 최대를 넘지 않으면서 자식이 존재하면서, 나보다 작으면 바꾸자
        if idx*2 < 100002 and queue[idx*2] and queue[idx] > queue[idx*2]:
            # 자식들 중에 작은 걸로 바꾸자
            if idx*2+1 < 100002 and queue[idx*2+1] and queue[idx*2] > queue[idx*2+1]:
                queue[idx], queue[idx*2+1] = queue[idx*2+1], queue[idx] 
                idx = idx*2+1
            else:
                queue[idx], queue[idx*2] = queue[idx*2], queue[idx] 
                idx *= 2
        # 왼쪽 자식이 부모보다 컸을 때, 오른쪽 자식이 나보다 크다면 내가 왼쪽 자식보다 클 수 없음
        # 인덱스는 최대가 넘지 않고 두번째 자식이 존재 해야함
        elif idx*2+1 < 100002 and queue[idx*2+1] and queue[idx] > queue[idx*2+1]:
            queue[idx], queue[idx*2+1] = queue[idx*2+1], queue[idx] 
            idx = idx*2+1
        else:
            # 자식이 부모보다 크다면 그만
            break
    # return res

for _ in range(N):
    order = int(input())
    if not order:
        popHeap()
        # print(popHeap())
    else:
        addHeap(order)
print(*ans, sep="\n")