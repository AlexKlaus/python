import re
import json


class NotANumberError(Exception):
    def __init__(self, text):
        self.text = text


numbers_list = []
while True:
    number = input("Введите число или 'q' для выхода: ")
    if number == 'q':
        break
    else:
        try:
            if re.match(r'(^\d+$)|(^\d+[.,]\d+$)', number):
                numbers_list.append(json.loads(number.replace(',', '.')))
            else:
                raise NotANumberError("Вы ввели не число!")
        except NotANumberError as err:
            print(err)
            continue

# проверка списка
print(numbers_list)
for n in numbers_list:
    print(n, type(n), sep=' - ')
