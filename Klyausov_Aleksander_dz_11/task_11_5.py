class Stock:
    """
    Склад
    stock_name - название склада
    equipment_in_stock{'объект оргтехники': количество, ...}
    """

    def __init__(self, stock_name):
        self.stock_name = stock_name
        self.equipment_in_stock = {}

    def add_equipment(self, equipment, quantity):
        """
        Добавляет оборудование на склад
        equipment - объект оборудования
        """
        self.equipment_in_stock[equipment] = self.equipment_in_stock.setdefault(equipment, 0) + quantity

    def give_away(self, equipment, quantity, where):
        """
        передача в определённое подразделение компании
        where - название подразделения куда передается оборудование
        """
        try:
            if self.equipment_in_stock[equipment] and self.equipment_in_stock[equipment] >= quantity:
                self.equipment_in_stock[equipment] -= quantity
                if self.equipment_in_stock[equipment] == 0:
                    self.equipment_in_stock.pop(equipment)
            else:
                print("На складе недостаточно необходимого оборудования!")
        except KeyError:
            print("Такого оборудования нет на складе!")


class OfficeEquipment:
    """
    Оргтехника
    model_name - название модели
    """

    def __init__(self, model_name):
        self.model_name = model_name
        self.type_of_equipment = ''

    def __str__(self):
        return self.model_name


class Printer(OfficeEquipment):
    """
    Принтеры
    printer_type - тип принтера (лазерный, струйный, ...)
    """

    def __init__(self, model_name, printer_type):
        super().__init__(model_name)
        self.printer_type = printer_type
        self.type_of_equipment = 'Принтер'


class Scanner(OfficeEquipment):
    """
    Сканеры
    scan_resolution - разрешение сканера
    """

    def __init__(self, model_name, scan_resolution):
        super().__init__(model_name)
        self.scan_resolution = scan_resolution
        self.type_of_equipment = 'Сканнер'


class Xerox(OfficeEquipment):
    """
    Ксерокс
    copy_speed - скорость копирования (копий в минуту)
    """

    def __init__(self, model_name, copy_speed):
        super().__init__(model_name)
        self.copy_speed = copy_speed
        self.type_of_equipment = 'Ксерокс'


# создаем обьекты оборудования
printer_x550 = Printer('x550', 'laser')
printer_a820 = Printer('a820', 'jet')
scanner_fast100500 = Scanner('fast100500', 600)
xerox_xr587 = Xerox('xr587', 20)

# Создаю объект класса Stock
stock = Stock('Склад')

# Добавляю оборудование на склад
stock.add_equipment(printer_a820, 10)
stock.add_equipment(printer_x550, 10)
stock.add_equipment(scanner_fast100500, 5)

# Проверяю наличие оборудования на складе
for k, v in stock.equipment_in_stock.items():
    print(k.type_of_equipment, k.model_name, '-', v, 'шт')

# Выдаем оборудование со склада
stock.give_away(printer_x550, 5, 'Офис')

# Проверка что на складе уменьшилось количество
for k, v in stock.equipment_in_stock.items():
    print(k.type_of_equipment, k.model_name, '-', v, 'шт')
