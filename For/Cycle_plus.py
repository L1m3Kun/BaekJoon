num = int(input())
tmp = num
count =0
while True:
    if tmp<10:
        tmp = int(str(tmp)+str(tmp))
    else:
        one = tmp%10
        ten = tmp//10
        tmp = int(str(one)+str((one+ten)%10))
    count +=1
    if tmp == num:
        break
print(count)