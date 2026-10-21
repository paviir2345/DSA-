def sortcolors(nums):
    zero = 0
    one = 0
    two = 0


    for num in nums:
        if num == 0:
            zero += 1
        elif num == 1:
            one += 1
        else:
            two += 1

    i = 0

    for j in range(zero):
        nums[i] = 0
        i += 1

   
    for j in range(one):
        nums[i] = 1
        i += 1

    for j in range(two):
        nums[i] = 2
        i += 1

    return nums


nums = [2, 0, 2, 1, 1, 0]
print(sortcolors(nums))