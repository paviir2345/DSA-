
def max_ones(mat):
    max_ones = -1
    row_index = 0

    for i in range(len(mat)):
        count = 0

        for j in range(len(mat[i])):
            if mat[i][j] == 1:
                count = count + 1

        if count > max_ones:
            max_ones = count
            row_index = i

    return [row_index, max_ones]


mat = [[0, 0, 0], [0, 1, 1]]
print(max_ones(mat))
