import sys
def is_han(n):
    n_list = list(map(int, list(str(n))))
    cnt = 1
    gab = -float('inf')
    if len(n_list) == 1:
        return 1
    else:    
        for i in range(1,len(n_list)):
            num = n_list[i]-n_list[i-1]
            if num ==gab:
                cnt += 1
            gab = num
        if cnt == (len(n_list)-1):
            return 1
        else:
            return 0


N = int(sys.stdin.readline().strip())
count =0
for i in range(1, N+1):
    if is_han(i):
        count += 1
print(count)