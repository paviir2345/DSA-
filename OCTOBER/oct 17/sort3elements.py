def sort3elements(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1

        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j = j - 1

        nums[j + 1] = key

    return nums


nums = [2, 0, 2, 1, 1, 0]
print(sort3elements(nums))