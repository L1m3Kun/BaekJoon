import sys
input = sys.stdin.readline

def dfs(i):
    global ans
    cycle = []  # 팀 후보
    while True:
        cycle.append(i) # 팀 후보 추가
        visited[i] = 1  # 방문 체크
        next = arr[i]   # 다음 팀 후보 저장
        if visited[next]:   # 다음 팀 후보가 이미 추가된 적 있으면 
            if next in cycle:     # 어디서부터 팀이 구성된건지 확인
                ans += len(cycle[cycle.index(next):])   # 그 숫자 확인
            return
        else:
            i = next    # 팀이 구성 안 되어 있으면 다음 후보로 이동

for _ in range(int(input())):
    N = int(input())
    arr = [0]+list(map(int, input().strip().split()))
    visited = [1] + [0] * N     # 방문
    ans = 0
    for i in range(1, N+1):   # 1번 주자부터 N번 주자까지 확인
        if not visited[i]:
            dfs(i)              # 아싸 찾기
    print(N - len(ans))   # 아싸는 모든 사람에서 인싸를 빼면 나옴
    