# cap = 3
# n = 7
# deliveries = [1, 1, 1, 1, 7, 5, 3]
# pickups =[1, 1, 1, 1, 1, 1, 1]

def solution(cap, n, deliveries, pickups):
    answer = 0
    pivot = n-1
    while pivot>=0:
        for i in range(pivot, -1, -1):
            if deliveries[i] or pickups[i]:
                answer += (i+1) * 2
                pivot = i
                break
        else:
            break
        maxG = maxT = cap
        for turn in range(pivot, -1, -1):
            if maxG and deliveries[turn]:
                if deliveries[turn] >= maxG:
                    deliveries[turn] -= maxG
                    maxG = 0
                else:
                    maxG -= deliveries[turn]
                    deliveries[turn] = 0
            if maxT and pickups[turn]:
                if pickups[turn] >= maxT:
                    pickups[turn] -= maxT
                    maxT = 0
                else:
                    maxT -= pickups[turn]
                    pickups[turn] = 0
            if not maxT and not maxG:
                break
    return answer


# def solution(cap, n, deliveries, pickups):
#     answer = 0
#     pivot = n-1
    
#     while pivot:
#         # for i in range(pivot-1, -1, -1):
#         #     if deliveries[i] or pickups[i]:    
#         #         answer += (i+1)*2
#         #         pivot = i+1
#         #         break
#         # else:
#         #     break
#         if deliveries[pivot] or pickups[pivot]:
#             print(pivot)
#             answer += (pivot +1)*2
#             maxG = maxT = cap
#             for i in range(pivot, -1, -1):
#                 if maxG and deliveries[i]:
#                     if deliveries[i] >= maxG:
#                         deliveries[i] -= maxG
#                         maxG = 0
#                     else:
#                         maxG -= deliveries[i]
#                         deliveries[i] = 0
#                 if maxT and pickups[i]:
#                     if pickups[i] >= maxT:
#                         pickups[i] -= maxT
#                         maxT = 0
#                     else:
#                         maxT -= pickups[i]
#                         pickups[i] = 0
#                 if not maxG and not maxT:
#                     break


#     return answer

# print(solution(cap, n, deliveries, pickups))

print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]), 16)
print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]), 30)
print(solution(4, 5, [8, 0, 8, 0, 4], [0, 0, 0, 0, 20]), 50)
print(solution(2, 2, [0, 1], [0, 4]), 8)
print(solution(2, 2, [0, 0], [0, 6]), 12)
print(solution(2, 2, [0, 0], [4, 0]), 4)
print(solution(2, 2, [5, 0], [0, 3]), 10)
print(solution(5, 3, [5, 0, 5], [0, 1, 10]), 16)
print(solution(5, 3, [5, 1, 5], [0, 1, 10]), 16)
print(solution(2, 3, [0, 6, 13], [19, 0, 1]), 54)
print(solution(2, 3, [4, 2, 1], [0, 4, 1]), 16)
print(solution(4, 5, [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]), 12)
print(solution(4, 4, [25, 24, 51, 0], [51, 0, 0, 49]), (13 * 4 + 6 * 2 + 6) * 2)
print(solution(4, 4, [25, 24, 51, 0], [51, 0, 0, 49]))