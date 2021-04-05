class Stock:
    """
    Склад
    name - название склада
    """

    def __init__(self, name):
        self.name = name


class OfficeEquipment:
    """
    Оргтехника
    model_name - название модели
    """

    def __init__(self, model_name):
        self.model_name = model_name


class Printer(OfficeEquipment):
    """
    Принтеры
    printer_type - тип принтера (лазерный, струйный, ...)
    """

    def __init__(self, model_name, printer_type):
        super().__init__(model_name)
        self.printer_type = printer_type


class Scanner(OfficeEquipment):
    """
    Сканеры
    scan_resolution - разрешение сканера dpi
    """

    def __init__(self, model_name, scan_resolution):
        super().__init__(model_name)
        self.scan_resolution = scan_resolution


class Xerox(OfficeEquipment):
    """
    Сканеры
    copy_speed - скорость копирования (копий в минуту)
    """

    def __init__(self, model_name, copy_speed):
        super().__init__(model_name)
        self.copy_speed = copy_speed


printer_1 = Printer('x550', 'laser')
printer_2 = Printer('a820', 'jet')
print(printer_1.printer_type)

scanner_1 = Scanner('fast100500', 600)
print(scanner_1.model_name)

xerox_1 = Xerox('xr587', 20)
print(xerox_1.copy_speed)
