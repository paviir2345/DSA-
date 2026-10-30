def two_sum(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        total = numbers[left] + numbers[right]

        if total == target:
            return [left + 1, right + 1]

        elif total < target:
            left = left + 1

        else:
            right = right - 1

    return []


numbers = [2, 7, 11, 15]
target = 9

print(two_sum(numbers, target))