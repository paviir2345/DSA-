def shiftGrid(grid, k):
    rows = len(grid)
    cols = len(grid[0])

    arr = []

    
    for i in range(rows):
        for j in range(cols):
            arr.append(grid[i][j])

    n = len(arr)
    result = []

    for i in range(n):
        new_index = (i + k) % n
        result.append(arr[new_index])

   
    answer = []
    index = 0

    for i in range(rows):
        row = []

        for j in range(cols):
            row.append(result[index])
            index = index + 1

        answer.append(row)

    return answer


grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
k = 1

print(shiftGrid(grid, k))