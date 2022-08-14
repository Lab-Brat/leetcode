# nums = [1,7,3,6,5,6]
# nums = [1,2,3]
# nums = [2,1,-1]
import timeit
import random
from array import array
nums = array('d', (random.randint(-1000,1000) for i in range(50000)))

start = timeit.default_timer()
def get_pivot(nums):
    for i, num in enumerate(nums):
        # print(nums[:i], nums[i+1:], sum(nums[:i]), sum(nums[i+1:]))
        if sum(nums[:i]) == sum(nums[i+1:]):
            return i
    return -1

print(get_pivot(nums))
stop = timeit.default_timer()
print(stop-start)
