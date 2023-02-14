import sys

for test_case in range(1, int(sys.stdin.readline().strip())+1):
    N, M = map(int, sys.stdin.readline().strip().split())
    primary = list(map(int, sys.stdin.readline().strip().split()))

    pointer = M
    count = 0

    while True:
        # 중요도 리스트에 요소가 있을때 없을때는 오류남
        if primary:
            # pointer 이용 포인터 차례일 때 최대 중요도면 끝
            if primary[0] == max(primary):
                count += 1  # 출력번째 세기
                if not pointer:
                    print(count)
                    break
                # 포인터 번째 아니면 계속
                else:
                    primary.pop(0)
                    # 포인터가 0일때는 없는데 혹시나 해서 만듦
                    if pointer:
                        pointer -= 1
                    else:
                        pointer = len(primary) - 1
            # 최대 중요도가 따로 있으면
            else:
                # 회전!
                primary.append(primary.pop(0))
                # 포인터도 회전!
                if pointer:
                    pointer -= 1
                else:
                    pointer = len(primary)-1
        # 무한루프 방지
        else:
            break

