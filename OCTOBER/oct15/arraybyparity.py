def arraybyparity(nums):
    n = len(nums)

    for i in range(n):
        for j in range(n - 1):
            if nums[j] % 2 == 1 and nums[j + 1] % 2 == 0:
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp

    return nums


nums = [3, 1, 2, 4]
print(arraybyparity(nums))

