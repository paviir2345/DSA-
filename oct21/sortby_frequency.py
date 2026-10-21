def sortby_frequency(nums):
    freq = {}

    
    for num in nums:
        if num in freq:
            freq[num] = freq[num] + 1
        else:
            freq[num] = 1

    
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):

            if freq[nums[i]] > freq[nums[j]]:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp

            elif freq[nums[i]] == freq[nums[j]]:
                if nums[i] < nums[j]:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp

    return nums


nums = [1, 1, 2, 2, 2, 3]
print(sortby_frequency(nums))