import urllib.request
from operator import itemgetter

url = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
requests = {}

with urllib.request.urlopen(url) as response:
    # Считаем сколько запросов сделано с каждго ip
    for line in response:
        ip = line.decode('utf-8').split(' ')[0]
        if requests.get(ip):
            requests[ip] += 1
        else:
            requests[ip] = 1
# Находим ip с максимальным количеством запросов
spammer = max(requests.items(), key=itemgetter(1))
print(f'Spammer is {spammer[0]} - {spammer[1]} requests')

# второе решение

# max_requests = 0
# for k, v in requests.items():
#     if v > max_requests:
#         max_requests = v
#         spammer = (k, v)
#
# print(f'Spammer is {spammer[0]} - {spammer[1]} requests')
