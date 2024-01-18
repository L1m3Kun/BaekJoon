# 10809 알파벳 찾기
import sys

def find_alpha(str):
    result = {}                     # Dictionary 생성
    for idx in range(97,123):       # key 값을 askii 코드를 이용하여 알파벳 순 저장
        result[chr(idx)]=-1         
    for i in range(len(str)):        
        if result[str[i]] == -1:    # value가 -1일 때만 번째수 저장
            result[str[i]] = i
        else:
            pass
    result = list(result.values())  # list 변환
    return result

S = list(sys.stdin.readline().strip())

for idx in range(len(find_alpha(S))):
    print(find_alpha(S)[idx], end = " ")