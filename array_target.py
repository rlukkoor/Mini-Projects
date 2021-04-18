nums = [3,2,4]
target = 6

length = len(nums)
for i in range (length - 1):    
	for j in range (i+1, length):
		if(nums[i] + nums[j] == target):
			print(str(nums[i]) + "," + str(nums[j]))