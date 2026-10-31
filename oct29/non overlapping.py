def erase_overlap(intervals):
    intervals = sorted(intervals, key=lambda x: x[1])

    count = 0
    end = intervals[0][1]

    for i in range(1, len(intervals)):

        if intervals[i][0] < end:
            count = count + 1
        else:
            end = intervals[i][1]

    return count


arr = [[1, 2], [2, 3], [3, 4], [1, 3]]
print(erase_overlap(arr))