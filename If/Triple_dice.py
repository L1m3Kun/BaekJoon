first, second, third = map(int, input().split())
if first == second == third:
    print(10000+first*1000)
elif first == second != third or first == third != second:
    print(1000+first*100)
elif first != second == third:
    print(1000+second*100)
elif first != second != third:
    print(max(first,second,third)*100)
   