def maxsubarray(nums):
    maxsum = nums[0]
    cursum = nums[0]

    for num in nums[1:]:
        cursum = max(num, cursum + num)
        maxsum = max(cursum, maxsum)
    return maxsum

if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(maxsubarray(nums))