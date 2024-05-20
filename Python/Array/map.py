def mpp(nums):
    hm = {}
    for i in range(len(nums)): 
       hm[nums[i]] = i

    return hm

if __name__ == "__main__":
    nums = [2,7,11,15]
    print(mpp(nums))