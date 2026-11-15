def single_num(nums):
    for num in nums:
        if nums.count(num) == 1:
            return num

nums = [4,1,2,1,2]
print(single_num(nums))
