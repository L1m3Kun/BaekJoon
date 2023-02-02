import sys
def bubble_sort(arr):
    for last in range(len(arr), 0, -1):
        for j in range(last):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

