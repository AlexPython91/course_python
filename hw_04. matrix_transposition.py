# Напишите функцию для транспонирования матрицы

def transpose_matrix(matrix):

    n = len(matrix)
    m = len(matrix[0])
    transposed_matrix = []

    for j in range(m):
        row = []
        for i in range(n):
            row.append(matrix[i][j])
        transposed_matrix.append(row)

    return transposed_matrix


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

transposed_matrix = transpose_matrix(matrix)
print(transposed_matrix)
