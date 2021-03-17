import os

# Создать структуру файлов и папок, как написано в задании 2
# (при помощи скрипта или «руками» в проводнике). Написать скрипт, который
# собирает все шаблоны в одну папку templates, например:
# |--my_project
#    ...
#    |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html
templates = []
for root, dirs, files in os.walk('my_project'):
    if root.rsplit('/', maxsplit=1)[-1] == 'templates' and root != 'my_project/templates':
        try:
            templates.append(os.path.join(root, dirs[0]))
        except IndexError:
            continue

root = 'my_project/templates'
if not os.path.exists('my_project/templates'):
    os.mkdir(root)

for path in templates:
    new_path = os.path.join(root, path.rsplit('/', maxsplit=1)[-1])
    if os.path.exists(path) and not os.path.exists(new_path):
        os.rename(path, os.path.join(new_path))
print(templates)
