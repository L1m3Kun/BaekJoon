def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    be = merge_sort(arr[:mid])
    af = merge_sort(arr[mid:])

    i = j = 0
    result = []

    while i < len(be) and j < len(af):
        if be[i] < af[j]:
            result.append(be[i])
            i += 1
        else:
            result.append(af[j])
            j += 1
    # if i == len(be):
    #     result += be[j:]
    # if j == len(af):
    #     result += af[i:]
    while i < len(be):
        result.append(be[i])
        i += 1
    while j < len(af):
        result.append(af[j])
        j += 1
    return result

arr = list(map(int, input().split()))

print(merge_sort(arr))