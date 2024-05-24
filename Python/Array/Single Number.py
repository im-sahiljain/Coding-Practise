def single(nums):
    seen = {}
    for i in range(len(nums)):
        if nums[i] in seen:
            seen[nums[i]] += 1
        else:
            seen[nums[i]] = 1
    for key,value in seen.items():
        if value == 1:
            return key
    return -1

if __name__ == "__main__":
    nums = [2,2,1]
    print(single(nums))