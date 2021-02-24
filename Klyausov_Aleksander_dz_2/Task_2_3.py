weather = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for item_id, item in enumerate(weather):
    # Если эдемент списка является числом или содержит символы но не кавычки, и прдыдущий элемент не кавычки
    if (item.isdigit() or (item.isalnum() is False and item != '"')) and weather[item_id - 1] != '"':
        if item.isalnum() is False:
            weather[item_id] = item.zfill(3)
        else:
            weather[item_id] = item.zfill(2)
        weather.insert(item_id, '"')
        weather.insert(item_id + 2, '"')

print(weather)
print(f"{weather[0]} {''.join(weather[1:4])} {weather[4]} " 
      f"{''.join(weather[5:8])} {' '.join(weather[8:12])} "
      f"{''.join(weather[12:15])} {weather[-1]}"
      )
