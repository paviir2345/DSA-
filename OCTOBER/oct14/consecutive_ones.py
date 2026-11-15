def consecutive_ones(nums, k):
    left = 0
    zeros = 0
    max_length = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zeros += 1

        while zeros > k:
            if nums[left] == 0:
                zeros -= 1
            left += 1

        length = right - left + 1

        if length > max_length:
            max_length = length

    return max_length


nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2

print(consecutive_ones(nums, k))