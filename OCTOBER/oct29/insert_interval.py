def insert(intervals, new_interval):
    result = []
    i = 0

    while i < len(intervals) and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i = i + 1

    while i < len(intervals) and intervals[i][0] <= new_interval[1]:

        if intervals[i][1] > new_interval[1]:
            new_interval[1] = intervals[i][1]

        i = i + 1

    result.append(new_interval)

    while i < len(intervals):
        result.append(intervals[i])
        i = i + 1

    return result


arr = [[1, 3], [6, 9]]
new_interval = [2, 5]

print(insert(arr, new_interval))