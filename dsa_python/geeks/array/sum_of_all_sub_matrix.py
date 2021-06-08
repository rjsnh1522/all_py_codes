

def sum_of_all_sub_matrix(matrix):
    i_row = len(matrix)
    j_col = len(matrix[0])
    sum_t = 0
    for i in range(0, i_row):
        for j in range(0, j_col):
            sum_t += matrix[i][j]
            for k in range(i, i_row):
                for l in range(j, i_row):
                    sum_t += matrix[k][l]
                    for a in range(i, k):
                        for b in range(j, l):
                             sum_t += matrix[a][b]

    return sum_t



a = [[1, 1], [1, 1]]
# print(sum_of_all_sub_matrix(a))


def sum_of_all_sub_matrix(matrix):
    i_row = len(matrix)
    j_col = len(matrix[0])
    sum_t = 0
    for i in range(i_row):
        for j in range(j_col):
            sum_t += (i+1)*(j+1)*(i_row - i)*(j_col - j) * matrix[i][j]

    return sum_t

print(sum_of_all_sub_matrix(a))
