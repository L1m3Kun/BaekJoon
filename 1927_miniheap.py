import sys
# import heapq
input = sys.stdin.readline

# queue = []
# N = int(input())
# for _ in range(N):
#     num = int(input())
#     heapq.heappush(queue, num) if num else print(heapq.heappop(queue)) if queue else print(0)
        

def append(n):
    pass
    tmp = n
    if queue:
        idx = 1
        while idx < len(queue):
            if tmp <queue[idx]:
                tmp, queue[idx] = queue[idx], tmp
                idx *= 2
            else:
                idx += 1
    queue.append(tmp)

def pop():
    if queue:
        print(queue.pop(1))
        idx = 1
        while idx < len(queue):
            if 
    else:
        print(0)    


N = int(input())
queue = [-1]
for _ in range(N):
    num = int(input())
    if num:
        append(num)
    else:
        pop()
    