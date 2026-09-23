# Two Sum Write a function two_sum(nums, target) that returns the indices of two numbers that add up to target, in O(n) time.

def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                continue
            if nums[i] + nums[j] == target:
                return [i, j]
    return None
    
def two_sum1(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

    return None


    
nums = [2, 7, 11, 15]

target = 9

print(two_sum1(nums, target))