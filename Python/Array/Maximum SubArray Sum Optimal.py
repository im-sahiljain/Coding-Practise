def maxsubarray(nums):
    maxsum = nums[0]
    cursum = nums[0]

    for i in range(1,len(nums)):
        cursum = max(cursum, cursum + nums[i])
        maxsum = max(cursum,maxsum)
    return maxsum

if __name__ == "__main__":
    nums = [-2,-3,-1,2,5,4,-3,-5]
    print(maxsubarray(nums))