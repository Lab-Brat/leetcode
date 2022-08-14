# nums = [1,2,3,4]
# nums = [1,1,1,1,1]
nums = [3,1,2,10,1]

for i, num in enumerate(nums):
    if i > 0:
        nums[i] = nums[i] + nums[i-1]

print(nums)