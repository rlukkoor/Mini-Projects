def merge_sort(array):
	if len(array) <= 1:
		return array
	result = []       
	mid = int(len(array) / 2)
	y = merge_sort(array[:mid])
	z = merge_sort(array[mid:])
	while (len(y) > 0) and (len(z) > 0):
		if y[0] > z[0]:
			result.append(z[0])
			z.pop(0)
		else:
			result.append(y[0])
			y.pop(0)
	result += y
	result += z
	return result

print(merge_sort([15, 13, 6, 9, 10, 2, 1, 3]))