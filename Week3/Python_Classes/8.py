def order007(nums):
    pattern = [0, 0, 7]
    
    for num in nums:
        if num == pattern[0]:
            pattern.pop(0)
            if not pattern:
                return True
    
    return False

listnum = input()
num_list = listnum.split()
num_list = [int(listnum) for listnum in num_list]
print(order007(num_list))