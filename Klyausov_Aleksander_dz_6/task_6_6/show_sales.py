def show_all_sales():
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        print(f.read())


def show_all_start_from_number(argv):
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        start = int(argv[1])
        for line in islice(f, start - 1, None):
            print(line.strip())


def show_from_to(argv):
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        start, end = int(argv[1]), int(argv[2])
        for line in islice(f, start - 1, end):
            print(line.strip())


if __name__ == '__main__':
    import sys
    from itertools import islice
    if len(sys.argv) == 1:
        exit(show_all_sales())
    elif len(sys.argv) == 2:
        exit(show_all_start_from_number(sys.argv))
    elif len(sys.argv) == 3:
        exit(show_from_to(sys.argv))
