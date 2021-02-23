prices = [57.8, 46.51, 97, 120, 185, 18284, 2519, 480, 333.3, 787.44, 30.01, 54.7, 65.89, 488.1, 666.6]
reverse_price = []
print("Id в начале:", id(prices))
prices_str = ''
n = 0   # счетчик

for p in sorted(prices):

    price = str(p).split('.')  # разделил цену на рубли и копейки
    if len(price) == 1:  # если копеек нет, то дописываем нули
        price.append('00')
    elif len(price[1]) == 1:  # если один знак после запятой, то дописываем один ноль
        price[1] = f'{price[1]}0'

    if n == len(prices)-1:  # если идет последний элемент списка то записываем без запятой
        prices_str += f'{price[0]} руб {price[1]} коп'  # заполняем строку в нужном формате
    else:
        prices_str += f'{price[0]} руб {price[1]} коп, '  # заполняем строку в нужном формате
    reverse_price.insert(0, f'{price[0]} руб {price[1]} коп')  # сразу создаем реверсирвованый список в нужном формате
    n += 1

print("Цены по возрастанию: ", prices_str)
print("Цены по убыванию: ", ', '.join(reverse_price))
print("Пять самых дорогих товаров: ", ', '.join(reverse_price[:5]))
print("Id в конце", id(prices))
