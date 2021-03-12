def edit_sales(argv):
    record_number, new_value = int(argv[1]), argv[2]
    with open('../task_6_6/bakery.csv', 'rb+') as f:
        for n, line in enumerate(f, 1):
            if n == record_number:
                start_position = f.tell() - len(line)  # Позиция курсора для записи нового значения
                f.seek(start_position)
                # Записываю новое значение поверх старого, заполняя пробелами строку до 20 символов
                f.write(f'{new_value}{" " * (20 - len(new_value))}\n'.encode("utf-8"))
                break
        if n < record_number:
            print("Записи не существует")


if __name__ == '__main__':
    import sys
    exit(edit_sales(sys.argv))
