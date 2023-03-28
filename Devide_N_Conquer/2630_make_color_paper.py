import sys
input = sys.stdin.readline

def check(paper):
    res = 0
    for i in range(len(paper)):
        res += sum(paper[i])
    return res

def solution(paper):
    global blue, white
    if len(paper) == 1:
        if paper[0] == 1:
            blue += 1
        else:
            white += 1
        return
    if check(paper) == len(paper)**2:
        blue += len(paper)**2
        return
    elif check(paper) == 0:
        white += len(paper)**2
        return
    else:
        half = len(paper)//2
        solution(paper[:half+1][:half+1])
        solution(paper[half:][:half+1])
        solution(paper[:half+1][half:])
        solution(paper[half:][half:])
        return 
        




N = int(input())
paper = [list(map(int, input().strip().split())) for _ in range(N)]

# solution(paper)
print(paper[:5][:5])