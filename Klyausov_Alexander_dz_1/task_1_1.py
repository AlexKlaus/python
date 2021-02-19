
duration = [53, 153, 4153, 400153, 3509743]

for dur in duration:
    human_time = ""
    print(f"{dur} сек:")
    if dur // 2629743:
        months = dur // 2629743
        dur %= 2629743
        human_time += f"{months} мес "
    if dur // 86400:
        days = dur // 86400
        dur %= 86400
        human_time += f"{days} дн "
    if dur // 3600:
        hours = dur // 3600
        dur %= 3600
        human_time += f"{hours} час "
    if dur // 60:
        minutes = dur // 60
        dur %= 60
        human_time += f"{minutes} мин "
    if dur:
        seconds = dur % 60
        human_time += f"{seconds} сек"
    print(human_time)
