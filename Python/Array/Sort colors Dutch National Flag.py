nums = [0,1,1,0,1,2,1,2,0,0,0]
low = 0
mid = 0
high = len(nums)-1

while mid <= high:
    if nums[mid] == 0:
        temp = nums[mid]
        nums[mid] = nums[low]
        nums[low] = temp
        low += 1
        mid += 1

    elif nums[mid] == 1:
        mid += 1

    elif nums[mid] == 2:
        temp = nums[mid]
        nums[mid] = nums[high]
        nums[high] = temp
        high -= 1

print(nums)
        
