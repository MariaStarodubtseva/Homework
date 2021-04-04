class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join('| '.join(map(str, i)) for i in self.matrix)

    def __add__(self, other):
        return Matrix([[sum(j) for j in zip(*i)] for i in zip(self.matrix, other.matrix)])


matrix_1 = Matrix([[2, 4, 8], [2, 7, 4], [5, 9, 7]])
matrix_2 = Matrix([[2, 5, 8], [3, 8, 1], [7, 4, 8]])

print(f'matrix_1:\n{matrix_1}')
print(f'\nmatrix_2\n{matrix_2}')
print(f'\nmatrix sum result:\n{matrix_1 +matrix_2}')
