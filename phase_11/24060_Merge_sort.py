import sys

def merge_sort_ready(arr = []):
	arr.sort()
	if len(arr) < 3:
		return arr
	else:
		q = int((arr[0] + arr[-1])/2)
		return arr, q

def merge_sort(arr:list, p, q, r):
	i = p
	j = q + 1
	t = 0
	tmp = []
	while i <= q and j <= r:
		if arr[i] <= arr[j]:
			tmp.append(arr[i])
		else:
			tmp.append(arr[j])
	while i <= q:
		tmp.append(arr[i]) 
	while j <= r:
		tmp.append(arr[j])
	return tmp 

lst = list(map(int,sys.stdin.readline().strip().split()))
lst, q = merge_sort_ready(lst)
print(merge_sort(lst, lst[0], q, lst[-1]))