from itertools import zip_longest, islice

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А'
]

tutor_klass = (tut for tut in zip_longest(tutors, klasses[:len(tutors)], fillvalue=None))

try:                            # Обработка исключения StopIteration
    print(type(tutor_klass))  # проверка что создал именно генераторр
    print(next(tutor_klass))
    print(*islice(tutor_klass, 6))  # истощаю генератор
    print(next(tutor_klass))
except StopIteration:
    print('Генератор истощен')

