class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f'Текущая скорость автомобиля: {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Превышение скорости! Текущая скорость: {self.speed}')
        else:
            print(f'Текущая скорость автомобиля: {self.speed}')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Превышение скорости! Текущая скорость: {self.speed}')
        else:
            print(f'Текущая скорость автомобиля: {self.speed}')


class PoliceCar(Car):
    pass


town_car = TownCar(70, 'red', 'Tesla', False)
sport_car = SportCar(200, 'red', 'Ferrari', False)
work_car = WorkCar(40, 'yellow', 'Volkswagen', False)
police_car = PoliceCar(60, 'white-blue', 'UAZ', True)

town_car.show_speed()
sport_car.show_speed()
print(police_car.is_police)
work_car.go()
work_car.turn('направо')
work_car.stop()
