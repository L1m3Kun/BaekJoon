cap = 1
n = 4
deliveries = [1, 1, 1, 0]
pickups =[0, 0, 0, 1]

def solution(cap, n, deliveries, pickups):
    answer = 0
    pivot = n-1
    
    while pivot >=0:
        # for i in range(pivot-1, -1, -1):
        #     if deliveries[i] or pickups[i]:    
        #         answer += (i+1)*2
        #         pivot = i+1
        #         break
        # else:
        #     break
        if deliveries[pivot] or pickups[pivot]:
            print(pivot)
            answer += (pivot +1)*2
            maxG = maxT = cap
            for i in range(pivot, -1, -1):
                if deliveries[i]:
                    if deliveries[i] >= maxG:
                        deliveries[i] -= maxG
                        maxG = 0
                    else:
                        maxG -= deliveries[i]
                        deliveries[i] = 0
                if pickups[i]:
                    if pickups[i] >= maxT:
                        pickups[i] -= maxT
                        maxT = 0
                    else:
                        maxT -= pickups[i]
                        pickups[i] = 0
                if not maxG and not maxT:
                    break

        pivot -=1
    return answer

print(solution(cap, n, deliveries, pickups))