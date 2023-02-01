import sys

def merge_sort(arr):
	if len(arr) == 1:
		return arr

	mid = len(arr) // 2
	arr_aft = merge_sort(arr[:mid])
	arr_bef = merge_sort(arr[mid:])
	result = []
	i = j = 0
	while i < len(arr_bef) and j < len(arr_aft):
		if arr_bef[i] < arr_aft[j]:
			result.append(arr_bef[i])
			count.append(arr_bef[i])
			i += 1
		else:
			result.append(arr_aft[j])
			count.append(arr_aft[j])
			j += 1
	while i < len(arr_bef):
		result.append(arr_bef[i])
		count.append(arr_bef[i])
		i += 1
	while j < len(arr_aft):
		result.append(arr_aft[j])
		count.append(arr_aft[j])
		j += 1
	return result

N, k = map(int, sys.stdin.readline().strip().split())
lst = list(map(int, sys.stdin.readline().strip().split()))
count = []
merge_sort(lst)

if len(count) >= k:
	print(count[k-1])
else:
	print(-1)


# def merge_sort(arr):
# 	if len(arr) == 1:
# 		return arr

# 	mid = len(arr) // 2
# 	arr_aft = merge_sort(arr[:mid])
# 	arr_bef = merge_sort(arr[mid:])
# 	result = []
# 	i = j = 0
# 	while i < len(arr_bef) and j < len(arr_aft):
# 		if arr_bef[i] < arr_aft[j]:
# 			result.append(arr_bef[i])
# 			i += 1
# 		else:
# 			result.append(arr_aft[j])
# 			j += 1
# 	result += arr_bef[i:]
# 	result += arr_aft[j:]
# 	return result

# def merge_sort(arr):
# 	def m_sort(start, finish):
# 		if start < finish:
# 			mid = (start + finish) //2
# 			m_sort(start, mid)
# 			m_sort(mid+1, finish)
# 			merge(start, mid, finish)

# 	def merge(start, mid, finish):
# 		i = start
# 		j = mid +1
# 		result = []
# 		while i <= mid and j <= finish:
# 			if arr[i] < arr[j]:
# 				result.append(arr[i])
# 				i += 1
# 			else:
# 				result.append(arr[j])
# 				j += 1

# 		while i <= mid:
# 			result.append(arr[i])
# 			i += 1
# 		while j <= finish:
# 			result.append(arr[j])
# 			j += 1
# 		for k in range(start, finish+1):
# 			arr[k] = result[k-start]

# 	return m_sort(0, len(arr))

# def merge_sort(arr, count):
# 	def sort(start, finish):
# 		if finish - start < 2:
# 			return

# 		mid = round((finish - start) / 2)
# 		sort(start, mid)
# 		sort(mid, finish)
# 		merge(start, mid, finish, count)

# 	def merge(start, mid, finish, count):
# 		result = []
# 		i = start
# 		j = mid + 1

# 		while i < mid and j < mid:
# 			count += 1
# 			if arr[i] < arr[j]:
# 				result.append(arr[i])
# 				i += 1
# 			else:
# 				result.append(arr[j])
# 				j += 1
# 		while i <= mid:
# 			count += 1
# 			result.append(arr[i])
# 			i += 1
# 		while j <= finish:
# 			count += 1
# 			result.append(arr[j])
# 			j += 1
# 		return result	
# 	return sort(0, len(arr))