
def duplicate(nums):
    seen = {}
    for i in range(len(nums)):
        if nums[i] in seen:
            return True
        else:
            seen[nums[i]] = 1
    return False
if __name__ == "__main__":
    nums = [1,2,3,1]
    print(duplicate(nums))