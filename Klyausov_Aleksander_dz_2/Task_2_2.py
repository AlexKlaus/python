weather = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

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
