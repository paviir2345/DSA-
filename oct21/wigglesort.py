def wigglesort(nums):
    n = len(nums)

    
    for i in range(1, n):
        key = nums[i]
        j = i - 1

        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1

        nums[j + 1] = key

    arr = nums.copy()

 
    left = (n - 1) // 2
    right = n - 1

    for i in range(n):
        if i % 2 == 0:
            nums[i] = arr[left]
            left -= 1
        else:
            nums[i] = arr[right]
            right -= 1

    return nums


nums = [1, 5, 1, 1, 6, 4]
print(wigglesort(nums))