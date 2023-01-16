num = input()
count=1
tmp =""
tmp = num
while True:
    if int(tmp)<10:
        tmp = tmp+tmp
       # print(tmp)
    else:
        tmp = list(tmp)[1]+str(int(list(tmp)[0])+int(list(tmp)[1]))
        #print(tmp)
    count+=1
    if num == tmp:
        break
print(count)