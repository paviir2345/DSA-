def three_sum(nums):
    n = len(nums)

   
    for i in range(n):
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp

    result = []

  
    for i in range(n - 2):

        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = n - 1

        
        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])

                left = left + 1
                right = right - 1

                
                while left < right and nums[left] == nums[left - 1]:
                    left = left + 1

                while left < right and nums[right] == nums[right + 1]:
                    right = right - 1

            elif total < 0:
                left = left + 1

            else:
                right = right - 1

    return result


nums = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums))