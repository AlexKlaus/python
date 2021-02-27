from random import randrange


def get_jokes(quantity, repeat=True):
    """
    Функция возвращает 'quantity' шуток, сформированных из двух случайных слов, взятых из трёх списков.
    :param quantity: 3
    :param repeat: False
    :return: ['дом позавчера мягкий', 'город сегодня веселый', 'автомобиль вчера зеленый']
    """
    all_words = {
        'nouns': ["автомобиль", "лес", "огонь", "город", "дом"],
        'adverbs': ["сегодня", "вчера", "завтра", "позавчера", "ночью"],
        'adjectives': ["веселый", "яркий", "зеленый", "утопичный", "мягкий"],
    }
    jokes = []
    for n in range(quantity):
        joke = list(map(lambda x: x[randrange(len(x))], all_words.values()))
        jokes.append(' '.join(joke))
        if not repeat:
            for joke_word, w_from_list in zip(joke, all_words.values()):
                if joke_word in w_from_list:
                    w_from_list.remove(joke_word)

    print(jokes)


get_jokes(quantity=3, repeat=False)
