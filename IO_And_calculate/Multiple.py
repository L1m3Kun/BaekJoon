a = int(input())
b = input()
for i in range(len(list(b))):
    print(int(list(b)[2-i])*a)  
print(a*int(b))