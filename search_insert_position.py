def searchInsert(nums, target):
    nums.append(target)         
    nums.sort()                 
    for i,j in enumerate(nums): 
        if target == j:         
            return i

print(searchInsert([1,3,5,6], 2))