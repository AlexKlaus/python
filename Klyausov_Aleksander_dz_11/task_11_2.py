class ZeroDivError(Exception):
    def __init__(self, text):
        self.text = text


a = int(input('Введите первое число: '))
while True:
    try:
        b = int(input('Введите второе число: '))
        if b == 0:
            raise ZeroDivError("Делить на 0 нельзя")
    except ZeroDivError as err:
        print(err)
    else:
        print(a / b)
        break
