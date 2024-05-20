def twosum(nums, target):
    mpp = {}
    for i in range(len(nums)):
        mpp[nums[i]] = i
        difference = target - nums[i]
        if difference in mpp:
            return [mpp[difference],i]
    return []

if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9
    print(twosum(nums, target))