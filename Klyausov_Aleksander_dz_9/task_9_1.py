from time import sleep, perf_counter


class TrafficLight:
    __color = None

    def running(self, color=None):
        """
        Если вызвать метод без параметра, то светофор переключится в следующий режим
        Если с параметром, то установится указаный в параметре цвет
        :param color:
        :return:
        """
        colors = ['красный', 'желтый', 'зеленый']
        # Если цвет не указан
        if not color:
            # Если светофор еще не был активирован или горел зеленый, то включаем красный
            if not TrafficLight.__color or colors.index(TrafficLight.__color) == 2:
                TrafficLight.__color = colors[0]
            else:
                TrafficLight.__color = colors[colors.index(TrafficLight.__color) + 1]
        else:
            # Порядок режимов светофора может нарушиться только если вводить цвета вручную
            # думаю проверку нужно делать здесь, иначе я не понимаю что требуется проверять в задании
            if color not in colors:
                raise ValueError("Неверный цвет!")
                # Если горел зеленый и указали не красный цвет, то ошибка
            elif (TrafficLight.__color == colors[2] and color != colors[0]) or \
                 (colors.index(TrafficLight.__color) >= colors.index(color)):
                raise ValueError("Нарушен порядок режимов!")
            TrafficLight.__color = color
        if TrafficLight.__color == colors[1]:
            sleep(2)
        else:
            sleep(7)


t_l = TrafficLight()

# Проверка автоматического переключения
for _ in range(10):
    start = perf_counter()
    t_l.running()
    print(f"Загорелся {t_l._TrafficLight__color} цвет светора.\n"
          f"Прошло {round(perf_counter() - start)} сек")
