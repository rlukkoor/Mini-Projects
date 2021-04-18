def quick_sort(array):
	if len(array) <= 1:
		return array
	less = []
	equal = []
	greater = []
	if(len(array) > 1):
		pivot = array[0]
		for x in array:
			if x < pivot:
				less.append(x)
			elif x == pivot:
				equal.append(x)
			elif x > pivot:
				greater.append(x)

		return quick_sort(less) + equal + quick_sort(greater)

print(quick_sort([15, 13, 6, 9, 10, 2, 1, 3]))