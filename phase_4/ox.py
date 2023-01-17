import sys

# 입력
T = int(sys.stdin.readline())   #test_case
for test_case in range(T):
    # ox 입력
    ox = list(sys.stdin.readline())
    # print(ox)
    # o 갯수 세기
    count = 0
    score = 0
    for val in ox:              # O일 때 count 증가
        if val == 'O':
            count += 1
        else:        # X일 때 count =0
            count = 0
        score += count
    print(score)