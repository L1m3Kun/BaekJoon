#test case
C = int(input())
for test_case in range(C):
    # 입력
    arr = list(map(int,input().split()))
    #N = arr[0]
    sum = 0
    for i in arr[1:]:
        sum += i
        #print(sum)
    average = sum / arr[0]
    #print(average)
    over_student = 0
    for i in arr[1:]:
        if i > average:
            over_student += 1
    total = round(over_student / (len(arr) - 1) * 100,3)
    print(f'{total:.3f}%')