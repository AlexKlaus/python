class Matrix:
    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists

    def __str__(self):
        result = '\n'.join([''.join(str(item) + " " * (9 - len(str(item))) for item in line)
                            for line in self.list_of_lists])
        return result

    def __add__(self, other):
        # Проверка равенства размерности матриц
        # Проверка равенства количества строк, и  равенства количества элементов
        if (len(self.list_of_lists) == len(other.list_of_lists)) and \
                (sum(len(line) for line in self.list_of_lists) == sum(len(line) for line in other.list_of_lists)):
            result = [
                [self_item + other_item for self_item, other_item in zip(self_line, other_line)]
                for self_line, other_line in zip(self.list_of_lists, other.list_of_lists)
            ]
            return Matrix(result)
        else:
            return "Матрицы должны быть равны!"


matrix_1 = Matrix([
    [1, -22, 3, 5],
    [4, 5, 6, 5],
    [1, 1, 1, 5]
])
matrix_2 = Matrix([
    [58, 16, 24, 5],
    [478, 23, 48, 48],
    [1, 1, 1, 58]
])
ma = matrix_1 + matrix_2
print(ma)
