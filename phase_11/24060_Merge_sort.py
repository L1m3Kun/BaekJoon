import sys


def merge_sort(arr):
	if len(arr) == 1:
		return arr
	else:
		arr_aft = merge_sort(arr[:int(len(arr) / 2)])
		arr_bef = merge_sort(arr[int(len(arr) / 2):])
		result = []
		for i in arr_aft
		if arr_aft[i] > arr_bef[j]:
			result.append()

		return



N, k = map(int, sys.stdin.readline().strip().split())
lst = list(map(int, sys.stdin.readline().strip().split()))
print(merge_sort(lst))