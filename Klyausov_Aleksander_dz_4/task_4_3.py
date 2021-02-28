from decimal import Decimal
from datetime import date
from requests import get


def currency_rates(currency):
    """
    Принимает в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
    и возвращающую дату, которая передаётся в ответе сервера и курс этой валюты по отношению к рублю.
    :param currency: USD
    :return: 2021-02-27: 1 USD = 74.4373 RUB
    """
    currency_data = get('http://www.cbr.ru/scripts/XML_daily.asp')
    currency_list = currency_data.text.split('Valute ID=')
    # Получаем дату из ответа и переворачиваем ее для возможности конвертировать ее в объект date
    response_date = reversed(currency_list[0].split('Date="')[1].split('" name')[0].split('.'))
    # Преобразуем в объект date
    response_date = date(*map(int, response_date))
    currency_value = {}

    for item in currency_list[1:]:
        char_code = item.split('<CharCode>')[1].split('</CharCode>')[0]
        currency_value[char_code] = Decimal(item.split('<Value>')[1].split('</Value>')[0].replace(',', '.'))

    print(f'{response_date}: '
          f'1 {currency.upper()} = {currency_value.get(currency.upper(), None).quantize(Decimal("1.00"))} RUB')


currency_rates('USD')
