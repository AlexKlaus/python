import os


# *(вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
# |--my_project
#    |--settings
#    |  |--__init__.py
#    |  |--dev.py
#    |  |--prod.py
#    |--mainapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--mainapp
#    |        |--base.html
#    |        |--index.html
#    |--authapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--authapp
#    |        |--base.html
#    |        |--index.html
def parse_yaml(yaml):
    """
    Функция читает структуру папок из файла .yaml и возвращает список с путями файлов и папок
    """
    with open(yaml, 'r', encoding='utf-8') as f:
        dirs = []
        for line in f:
            if line.startswith('|--'):
                dirs.append(line.strip('|--').strip())
            elif line.startswith('   |--'):
                dirs.append(os.path.join(dirs[0], line.strip('   |--').strip()))
            elif line.startswith('   |  |--'):
                dirs.append(os.path.join([x for x in dirs if len(x.split('/')) == 2][-1],
                                         line.strip('   |  |--').strip()))
            elif line.startswith('   |     |--'):
                dirs.append(os.path.join([x for x in dirs if len(x.split('/')) == 3][-1],
                                         line.strip('   |     |--').strip()))
            elif line.startswith('   |        |--'):
                dirs.append(os.path.join([x for x in dirs if len(x.split('/')) == 4][-1],
                                         line.strip('   |        |--').strip()))
        return dirs


def make_dirs(dirs):
    """Функция получает список с путями файлов и папок, и создает эти файлы и папки"""
    for d in dirs:
        if not os.path.exists(d) and '.' not in d:
            os.makedirs(d)
        elif not os.path.exists(d):
            file = open(d, 'w')
            file.close()
    exit(0)


print(make_dirs(parse_yaml('config.yaml')))
