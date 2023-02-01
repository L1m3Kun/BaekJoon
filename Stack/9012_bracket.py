import sys

for bracket in range(int(sys.stdin.readline())):
    bracket = list(sys.stdin.readline().strip())
    # count 설정
    count = 0
    for idx in range(len(bracket)):
        # 만약 ( 이면 +1, )이면 -1
        if bracket[idx] == '(':
            count += 1
        elif bracket[idx] == ')':
            count -= 1
        # 음수가 되면  NO, for 문도 정지
        if count < 0:
            print('NO')
            break    
    else:
        # 다 돌았을때 숫자가 같으면(중간에 음수가 되는 것 없이) YES
        if count == 0:
            print('YES')
        else:
            print('NO')
