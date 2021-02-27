# *(вместо задачи 1) Доработать предыдущую функцию в num_translate_adv():
# реализовать корректную работу с числительными, начинающимися с заглавной
# буквы — результат тоже должен быть с заглавной. Например:
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"
def num_translate_adv(word):
    """Функция переводит числительные слова от 1 до 10 с английского на русский язык"""
    numbers_dict = {'one': 'один',
                    'two': 'два',
                    'three': 'три',
                    'four': 'четыре',
                    'five': 'пять',
                    'six': 'шесть',
                    'seven': 'семь',
                    'eight': 'восемь',
                    'nine': 'девять',
                    'ten': 'десять'}

    if word.istitle():
        print(numbers_dict.get(word.lower(), 'None').capitalize())
    else:
        print(numbers_dict.get(word.lower(), 'None'))


num_translate_adv('Two')
num_translate_adv('six')
num_translate_adv('TEN')
num_translate_adv('Five')
num_translate_adv('twelve')
