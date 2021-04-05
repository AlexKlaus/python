class Cell:
    def __init__(self, number_of_cells):
        self.number_of_cells = number_of_cells

    def __add__(self, other):
        return Cell(self.number_of_cells + other.number_of_cells)

    def __sub__(self, other):
        if self.number_of_cells - other.number_of_cells > 0:
            return Cell(self.number_of_cells - other.number_of_cells)
        else:
            return "Разность количества ячеек меньше либо равна нулю"

    def __mul__(self, other):
        return Cell(self.number_of_cells * other.number_of_cells)

    def __floordiv__(self, other):
        return Cell(self.number_of_cells // other.number_of_cells)

    def __truediv__(self, other):
        return Cell(self.number_of_cells // other.number_of_cells)

    def __str__(self):
        return str(self.number_of_cells)

    def make_order(self, cells_in_row):
        result = ['*' * cells_in_row for _ in range(self.number_of_cells // cells_in_row)]
        if self.number_of_cells % cells_in_row:
            result.append(f'{"*" * (self.number_of_cells % cells_in_row)}')
        return r'\n'.join(result)


cell_1 = Cell(18)
cell_2 = Cell(8)
print(cell_1.make_order(5))

print(f'Количество ячеек клетки 1 = {cell_1}')
print(f'Количество ячеек клетки 2 = {cell_2}')

print(f'Сложение: {cell_1 + cell_2}')
print(type(cell_1 + cell_2))

print(f'Вычитание: {cell_1 - cell_2}')
print(type(cell_1 - cell_2))

print(f'Умножение: {cell_1 * cell_2}')
print(type(cell_1 * cell_2))

print(f'Деление __floordiv__: {cell_1 // cell_2}')
print(type(cell_1 // cell_2))

print(f'Деление __truediv__ как целочисленное: {cell_1 / cell_2}')
print(type(cell_1 / cell_2))
