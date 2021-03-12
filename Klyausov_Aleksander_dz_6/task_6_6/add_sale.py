def add_sale(argv):
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        # Записываю цену в строку длиной 20 символов, пустое пространство заполняю пробелами
        # это упростит дальнейшее редактирование цен, если количество символов в цене увеличится
        # не придется переписывать весь файл
        new_line = f'{argv[1]}{" " * (20 - len(argv[1]))}\n'
        f.write(new_line)


if __name__ == '__main__':
    import sys
    exit(add_sale(sys.argv))
