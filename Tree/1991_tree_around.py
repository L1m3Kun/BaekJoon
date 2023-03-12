import sys
input = sys.stdin.readline


def preorder(spot):         # 전위순회
    if spot in tree.keys(): 
        print(spot, end='')
        preorder(tree[spot][0])
        preorder(tree[spot][1])
    return

def inorder(spot):          # 중위 순회
    if spot in tree.keys():
        inorder(tree[spot][0])
        print(spot, end='')
        inorder(tree[spot][1])
    return

def postorder(spot):        # 후위 순회
    if spot in tree.keys():
        postorder(tree[spot][0])
        postorder(tree[spot][1])
        print(spot, end='')
    return

N = int(input())
arr = [list(input().strip().split()) for _ in range(N)]
tree = {}
# 입력저장
for i in range(N):
    for j in range(1, 3):
        if arr[i][0] not in tree.keys():
            tree[arr[i][0]] = list(arr[i][j])
        else:
            tree[arr[i][0]].append(arr[i][j])
preorder('A')
print()     # 띄어쓰기
inorder('A')
print()     # 띄어쓰기
postorder('A')