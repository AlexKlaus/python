import os

# Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp
root_dir = 'my_project'
dirs = ['setting', 'mainapp', 'adminapp', 'authapp']

for d in dirs:
    dir_path = os.path.join(root_dir, d)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
