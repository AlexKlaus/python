weather = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print("Id:", id(weather))

for item_id, item in enumerate(weather):
    # Если эдемент списка является числом или спецсимволом но не кавычки, и прдыдущий элемент не кавычки
    if (item.isdigit() or (item.isalnum() is False and item != '"')) and weather[item_id - 1] != '"':
        # Если элемент списка содержит спецсимвол и оставшаяся меньше двух символов, то дописываем ноль
        if item.isalnum() is False and len(item[1:]) < 2:
            weather[item_id] = f"{item[0]}0{item[1:]}"
        # Если число состои менее чем из двух символов, дописываем ноль
        elif len(item) < 2:
            weather[item_id] = f"0{item}"
        weather.insert(item_id, '"')
        weather.insert(item_id + 2, '"')

print(f"{weather[0]} {''.join(weather[1:4])} {weather[4]} " 
      f"{''.join(weather[5:8])} {' '.join(weather[8:12])} "
      f"{''.join(weather[12:15])} {weather[-1]}"
      )

# # # Старый код:
# # Обработка списка
# for item in weather:
#
#     # Если строка содержит знаки '+' или '-', и оставшаяса чать является числом, и длина числа меньше 2
#     if ('+' in item or '-' in item) and item[1:].isdigit() and len(item[1:]) < 2:
#         weather.insert((weather.index(item)), '"')  # добавлем кавычки
#         weather.insert((weather.index(item)+1), '"')
#         weather[weather.index(item)] = f"{item[0]}0{item[1:]}"  # добавляем нуль до двух разрядов
#
#     # Если строка является числом и длина меньше 2, то добавляем разрядность и кавычки
#     elif item.isdigit() and len(item) < 2:
#         weather.insert((weather.index(item)), '"')  # добавлем кавычки
#         weather.insert((weather.index(item) + 1), '"')
#         weather[weather.index(item)] = f"0{item}"  # добавляем нуль до двух разрядов
#
#     # Если строка является числом, и перед нет кавычек, то ставим кавычки
#     # Если не делать проверку на кавычки, то после первой итерации происходит зацикливание
#     # т.к. после добавления кавычек число смещается.
#     elif item.isdigit() and (weather[weather.index(item) - 1] != '"'):
#         weather.insert((weather.index(item)), '"')  # добавлем кавычки
#         weather.insert((weather.index(item) + 1), '"')
#
# # Формируем строку из обработанного списка
# weather_str = f"{weather[0]} {''.join(weather[1:4])} {weather[4]} " \
#               f"{''.join(weather[5:8])} {' '.join(weather[8:12])} " \
#               f"{''.join(weather[12:15])} {weather[-1]}"
# print(weather_str)
# print("Id:", id(weather))
