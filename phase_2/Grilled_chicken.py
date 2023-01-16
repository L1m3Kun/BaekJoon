a, b = map(int, input().split())
c = int(input())
if b+c>=60:
    minute = b+c

    while minute>=60:
        minute -= 60
        a += 1
        if a==24:
            a = 0

            
    
else:
    minute = b+c

print(a, minute)