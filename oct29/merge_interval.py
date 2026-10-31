def merge(intervals):
    intervals = sorted(intervals, key=lambda x: x[0])

    result = []
    result.append(intervals[0])

    for i in range(1, len(intervals)):
        last = result[len(result) - 1]

        if intervals[i][0] <= last[1]:
            if intervals[i][1] > last[1]:
                last[1] = intervals[i][1]
        else:
            result.append(intervals[i])

    return result


arr = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge(arr))