import sys      # input으로 쓰면 시간초과가 나옴
N = int(sys.stdin.readline())
num_lst = []
for _ in range(N):
    num_lst.append(int(sys.stdin.readline()))
for num in sorted(num_lst):
    print(num)