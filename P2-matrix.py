class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        """Add two matrices"""
        result = []
        for i in range(3):
            row = [self.matrix[i][j] + other.matrix[i][j] for j in range(3)]
            result.append(row)
        return Matrix(result)

    def __mul__(self, other):
        """Multiply two matrices"""
        result = [[0 for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    result[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return Matrix(result)

    def transpose(self):
        """Transpose the matrix"""
        result = [[self.matrix[j][i] for j in range(3)] for i in range(3)]
        return Matrix(result)

    def __str__(self):
        """Return the string representation of the matrix"""
        return '\n'.join(['\t'.join(map(str, row)) for row in self.matrix])


matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

print("Matrix 1 + Matrix 2:")
result_add = matrix1 + matrix2
print(result_add)

print("\nMatrix 1 * Matrix 2:")
result_mul = matrix1 * matrix2
print(result_mul)

print("\nTranspose of Matrix 1:")
result_transpose = matrix1.transpose()
print(result_transpose)
