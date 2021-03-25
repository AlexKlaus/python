class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_weight(self, m_weight, thickness):
        return f'{round(self._length * self._width * m_weight * thickness / 1000)} т.'


road = Road(5000, 20)
print(road.calc_weight(25, 5))
