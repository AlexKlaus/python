from itertools import zip_longest

with open('users_hobby.txt', 'w', encoding='utf-8') as f_users_hobby, \
        open('users.csv', 'r', encoding='utf-8') as f_users, \
        open('hobby.csv', 'r', encoding='utf-8') as f_hobby:

    for u, h in zip_longest(f_users, f_hobby, fillvalue='None'):
        if u == 'None':  # Если фамилии закончились а хобби осталась, то выходим с кодом 1
            exit(1)
        else:
            f_users_hobby.write(f'{u.strip()}: {h.strip()}\n')
