from heapq import heappop, heappush  

def heap_sort(array):
	if len(array) <= 1:
		return array
	heap = []  
	for ele in array:
		heappush(heap, ele)
	sort = []
	while heap:
		sort.append(heappop(heap))
	return sort  

print(heap_sort([15, 13, 6, 9, 10, 2, 1, 3]))