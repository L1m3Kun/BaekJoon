# 2470 두 용액
import sys
input = sys.stdin.readline


def two_pointer():
    N = int(input())
    arr = sorted(list(map(int, input().split())))
    s,e = 0, N-1
    pair = tuple()
    minv = 1_000_000_001*N
    while s<e:
        if minv > abs(arr[s] + arr[e]):
            minv = abs(arr[s] + arr[e])
            pair = tuple([arr[s], arr[e]])

        if arr[s] + arr[e] < 0:
            s += 1
        elif arr[s] + arr[e] > 0:
            e -= 1
        else:
            break

    print(*pair)


# def binary_search():
#     N = int(input())
#     arr = sorted(list(map(int, input().split())))
#     if arr[0] >= 0:
#         print(arr[0], arr[1])
#         return
#     if arr[-1] <= 0:
#         print(arr[-2], arr[-1])
#         return
#     minv = 1_000_000_001 * N
#     for i in range(N-1):
#         liquid = -arr[i]
#         candidate = arr[i+1:]
#         s,e = 0, N-i-1
#         while s<e:
#             mid = (s+e)//2
#             if candidate[mid] == liquid:
#                 print(-liquid, candidate[mid])
#                 return
#             if candidate[mid] > liquid:
#                 if minv > abs(-liquid+candidate[mid]):
#                     minv = abs(-liquid+candidate[mid])
#                     pair = tuple([-liquid, candidate[mid]])
#                 e = mid - 1
#             else:
#                 if minv > abs(-liquid+candidate[mid]):
#                     minv = abs(-liquid+candidate[mid])
#                     pair = tuple([-liquid, candidate[mid]])
#                 s = mid + 1
#     print(*pair)
        
    
if __name__ == "__main__":
    # binary_search()
    two_pointer()