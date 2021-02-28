from decimal import Decimal
from requests import get


def currency_rates(currency):
    """
    Принимает в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
    и возвращающую курс этой валюты по отношению к рублю.
    :param currency: USD
    :return: 74.4373
    """
    currency_data = get('http://www.cbr.ru/scripts/XML_daily.asp')
    currency_list = currency_data.text.split('Valute ID=')
    currency_value = {}

    for item in currency_list[1:]:
        char_code = item.split('<CharCode>')[1].split('</CharCode>')[0]
        currency_value[char_code] = Decimal(item.split('<Value>')[1].split('</Value>')[0].replace(',', '.'))

    print(f'1 {currency.upper()} = {currency_value.get(currency.upper(), None).quantize(Decimal("1.00"))} RUB')


currency_rates('usd')
