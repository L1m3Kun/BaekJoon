import sys
div_arr = []
for i in range(10):
    num = int(sys.stdin.readline())
    div_arr.append(num%42)
div_arr = set(div_arr)
print(len(div_arr))