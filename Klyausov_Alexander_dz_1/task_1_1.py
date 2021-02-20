
# duration = [53, 153, 4153, 400153, 3509743]
sec = [31556926, 2629743, 86400, 3600, 60, 1]
human_format = ['год', 'мес', 'дн', 'час', 'мин', 'сек']
human_time = ""
duration = int(input("Введите длительность времени в секундах: "))

for idx in range(0, len(sec)):
    if duration // sec[idx]:
        human_time += f"{duration // sec[idx]} {human_format[idx]} "
        duration %= sec[idx]

print(human_time)
