nums = [0,1,2,0,1,2,1,2,0,0,0,1]
c0,c1,c2=0,0,0
for i in range(len(nums)):
    if nums[i] == 0:
        c0 += 1
    elif nums[i] == 1:
        c1 += 1
    else:
        c2 += 1
print(c0, c1,c2)

for i in range(len(nums)):
    if i < c0:
        nums[i] = 0
    elif i < c0+c1:
        nums[i] = 1
    else:
        nums[i] = 2

print(nums)
