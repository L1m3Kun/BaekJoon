import sys
input = sys.stdin.readline

def solution(n, k, arr):
    plug = [0] * n      # 멀티탭
    cnt = 0             # 교체 횟수
    idx = 0             # 인덱스
    if n == 1:          # 멀티탭이 1구이면 바로 옆이 같은 경우 말고는 카운트
        for i in range(1, k):
            if arr[i] != arr[i-1]:
                cnt +=1
        return cnt
    # 멀티탭이 2구 이상일 때
    for i in range(k):
        # 다음 대기순이 플러그에 없으면
        if not arr[i] in plug:
            # 플러그 빈자리가 있으면 바로 넣기
            if idx == n:
                # 다음에 같은 대기순이 있는지 확인하기 용
                need = [0] * n
                # 다음 순번 중 같은 값 기록
                for j in range(n):
                    for l in range(i+1, k):
                        if plug[j] == arr[l]:
                            need[j] = l
                            break
                # 만약 필요없는게 있으면 그자리에 넣기
                if 0 in need:
                    plug[need.index(0)] = arr[i]
                    cnt += 1
                # 필요없는게 없으면 가장 나중에 오는 순번껄로 바꾸기
                else:
                    plug[need.index(max(need))] = arr[i]
                    cnt += 1
                
            else:
                plug[idx] = arr[i]
                idx += 1
    return cnt

N, K = map(int, input().strip().split())
request = list(map(int, input().strip().split()))
print(solution(N, K, request))