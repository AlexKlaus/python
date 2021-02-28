# Задание 4
# Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли. Например:
# > python task_4_5.py USD
# 75.18, 2020-09-05

from decimal import Decimal
from datetime import date

from requests import get


def currency_rates(argv):
    """
    Принимает в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
    и возвращающую дату, которая передаётся в ответе сервера и курс этой валюты по отношению к рублю.
    :param argv:
    :return: 70.20, 2021-02-27
    """
    currency_data = get('http://www.cbr.ru/scripts/XML_daily.asp')
    currency_list = currency_data.text.split('Valute ID=')
    # Получаем дату из ответа и переворачиваем ее для возможности конвертировать ее в объект date
    response_date = reversed(currency_list[0].split('Date="')[1].split('" name')[0].split('.'))
    # Преобразуем в объект date
    response_date = date(*map(int, response_date))
    currency_value = {}
    program, currency = argv

    for item in currency_list[1:]:
        char_code = item.split('<CharCode>')[1].split('</CharCode>')[0]
        currency_value[char_code] = Decimal(item.split('<Value>')[1].split('</Value>')[0].replace(',', '.'))

    print(f'{currency_value.get(currency.upper(), None).quantize(Decimal("1.00"))}, {response_date}')


if __name__ == '__main__':
    import sys

    exit(currency_rates(sys.argv))
