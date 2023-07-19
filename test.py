# 행렬 테두리 회전하기     
def solution(rows, columns, queries):
    answer = []
    matrix = [[j + columns*i for j in range(1, columns+1)] for i in range(rows)]
    
    for quest in queries:
        # print(quest)
        i, j = quest[0]-1, quest[1]-1
        tmp = matrix[i+1][j]
        while True:
            
            tmp, matrix[i][j]  = matrix[i][j], tmp
            if i == quest[0]-1:
                if j == quest[1]-1:
                    j += 1
                elif j == quest[3]-1:
                    i += 1
                else:
                    j += 1
            elif j == quest[3]-1:
                if i ==quest[2]-1:
                    j -=1
                else:
                    i +=1
            elif i == quest[2]-1:
                if j == quest[1]-1:
                    i -= 1
                else:
                    j -=1 
            elif j == quest[1]-1:
                if i == quest[0]-1:
                    break
                else:
                    i -= 1
            if i == quest[0]-1 and j == quest[1] -1:
                break
    for i in range(rows):
        print(matrix[i])
    for i in range(rows):
        for j in range(columns):
            print(matrix[i][j], end=", ")
            print((j+1)+columns*i)
            if matrix[i][j] != (j+1)+columns*i:
                answer.append((j+1)+columns*i)
    answer.sort()
    # print(answer)
    return answer

solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]])