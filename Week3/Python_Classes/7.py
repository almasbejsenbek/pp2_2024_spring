def func(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

nums = input()
numbers = nums.split() 
numbers = [int(nums) for nums in numbers]
result = func(numbers)
print(result)