def main(argv):
    users, hobbies, users_hobbies = argv[1:]
    with open(users_hobbies, 'w', encoding='utf-8') as f_users_hobby, \
            open(users, 'r', encoding='utf-8') as f_users, \
            open(hobbies, 'r', encoding='utf-8') as f_hobby:

        for u, h in zip_longest(f_users, f_hobby, fillvalue='None'):
            if u == 'None':  # Если фамилии закончились а хобби осталась, то выходим с кодом 1
                return 1
            else:
                f_users_hobby.write(f'{u.strip()}: {h.strip()}\n')
        return 0


if __name__ == '__main__':
    import sys
    from itertools import zip_longest
    exit(main(sys.argv))
