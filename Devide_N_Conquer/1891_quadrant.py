import sys
input = sys.stdin.readline

def solution(s, i, x_start, x_end, y_start, y_end):
    
    if i == N:
        # print(x_start, x_end, y_start, y_end)
        # arr.append((x_start - x, y_start - y))
        print(x_start, y_start)
        arr[0]=x_start + x
        arr[1] = y_start - y
        return
    if s[i] == '1':
        solution(s, i+1, (x_start+x_end)//2+1, x_end, y_start, (y_start+y_end)//2)
    elif s[i] == '2':
        solution(s, i+1, x_start, (x_start+x_end)//2, y_start, (y_start+y_end)//2)
    elif s[i] == '3':
        solution(s, i+1, x_start, (x_start+x_end)//2, (y_start+y_end)//2+1, y_end)
    else:
        solution(s, i+1, (x_start+x_end)//2+1, x_end, (y_start+y_end)//2+1, y_end)

    return

def find_after(target_x, target_y):
    after = ''
    for d in range(1,N+1):
        if (1<<(N-d))<=target_x<=(1<<N) and 0<=target_y<=(1<<(N-d)):
            after += '1'
        elif 0<=target_x<=(1<<(N-d)) and 0<=target_y<=(1<<(N-d)):
            after += '2'
        elif 0<=target_x<=(1<<(N-d)) and (1<<(N-d))<=target_y<=(1<<N):
            after += '3'
        elif (1<<(N-d))<=target_x<=(1<<N) and (1<<(N-d))<=target_y<=(1<<N):
            after += '4'
    return after


N, start = input().split()
N = int(N)
x, y = map(int, input().split())
arr = [0]*2
solution(start, 0, 0, (1<<N)-1, 0, (1<<N)-1)
print(arr)
print(find_after(arr[0],arr[1]))

