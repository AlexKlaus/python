from itertools import zip_longest
import json

with open('users.csv', 'r', encoding='utf-8') as f_users, \
        open('hobby.csv', 'r', encoding='utf-8') as f_hobby, \
        open('users_hobbies.json', 'w', encoding='utf-8') as f_users_hobbies:

    users = [user.strip().replace(',', ' ') for user in f_users]
    hobbies = [hobby.strip().split(',') for hobby in f_hobby]

    if len(users) < len(hobbies):
        exit(1)
    else:
        users_hobbies = {user: hobby for user, hobby in zip_longest(users, hobbies, fillvalue=None)}
        json.dump(users_hobbies, f_users_hobbies)  # Записать словарь в файл


# Проверка файла
with open('users_hobbies.json', 'r', encoding='utf-8') as f:
    users_hobbies = json.load(f)
    print(type(users_hobbies), users_hobbies)
