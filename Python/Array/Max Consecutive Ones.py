nums = [1,0,1,1,0,1]
max_count = 0
curr_count = 0

for i in range(len(nums)):
    if nums[i] == 1:
        curr_count += 1
    else:
        curr_count = 0
    max_count = max(max_count,curr_count)

print(max_count)


