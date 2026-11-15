def merge(intervals):

    intervals = merge_sort(intervals, 0)

    result = []

    for i in range(len(intervals)):

        if len(result) == 0:
            result.append(intervals[i])

        else:
            last = result[len(result) - 1]

            if intervals[i][0] <= last[1]:

                if intervals[i][1] > last[1]:
                    last[1] = intervals[i][1]

            else:
                result.append(intervals[i])

    return result


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

print(merge(intervals))