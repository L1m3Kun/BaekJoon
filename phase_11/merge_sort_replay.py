def merge_sort(start, finish):
    if finish == (start + 1):
        return
    mid = (start + finish) // 2
    merge_sort(start, mid)
    merge_sort(mid, finish)

    i = start
    j = mid
    tmp = []

    while i < mid and j < finish:
        if arr[i] < arr[j]:
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            j += 1
    if i == mid:
        tmp += arr[j:]
    elif j == finish:
        tmp += arr[i:]
    for idx in range(start, finish):
        arr[idx] = tmp[idx-start]


arr = list(map(int, input().split()))
print(arr)
merge_sort(0, len(arr))
print(arr)