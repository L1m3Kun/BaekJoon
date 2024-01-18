# 1002 터렛
import sys
input = sys.stdin.readline


def solution(x1:int, y1:int, r1:int, x2:int, y2:int, r2:int):
    rad_sum = (r1+r2)**2
    rad_dis = (r1 - r2)**2
    distance= (x1-x2)**2 + (y1-y2)**2
    
    # 동심원
    if distance == 0:
        # 반지름이 같으면 무한대
        # 반지름이 같지 않으면 접점 없음
        return -1 if r1 == r2 else 0
    # 반지름의 차와 반지름의 합 사이에 거리가 있을 때
    # 접점 2개
    if rad_dis < distance < rad_sum:
        return 2
    # 반지름의 차나 반지름의 합과 거리가 같을 때
    # 내접 or 외접 -> 접점 1개
    if rad_sum == distance or rad_dis == distance:
        return 1
    # 그 외의 경우
    # 반지름의 차나 반지름의 합보다 거리가 작을 때
    # 접점이 생기지 않음
    return 0
    
    
        

if __name__ == "__main__":
    for _ in range(int(input())):
        print(solution(*list(map(int, input().split()))))