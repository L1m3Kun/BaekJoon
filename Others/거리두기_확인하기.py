def check(y, x, arr):
    for i in range(3):
        for j in range(abs(i)-2, 3-abs(i)):
            if 0<=y + i < 5 and 0<= x+j < 5 and  arr[y+i][x+j] == 'P':
                if abs(i) + abs(j) == 1:
                    print(y,x, 1)
                    return 1
                if i == 0 and j != 0 and arr[y][x+j//2] != 'X':
                    print(y,x, 2)
                    return 1
                if i != 0 and j == 0 and arr[y+i//2][x] != 'X':
                    print(y,x, 3)
                    return 1
                
                if i != 0 and j != 0:
                    if arr[y+1][x] != 'X':
                        print(y, x, 6)
                        return 1
                    else:
                        if j<0 and arr[y][x-1] != 'X':
                            print(y, x, 4)
                            return 1
                        elif j>0 and arr[y][x+1] != 'X':
                            print(y, x, 5)
                            return 1

def solution(places):
    answer = []
    for room in range(5):
        print('page', room+1)
        i= j = 0
        while i< 5 and j <5:
            if places[room][i][j] == 'P':
                if check(i, j, places[room]):
                    answer.append(0)
                    break
            if j <4:
                j += 1
            elif j == 4:
                i += 1
                j = 0
        else:
            answer.append(1)
        print()
    return answer

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

print(solution(places))