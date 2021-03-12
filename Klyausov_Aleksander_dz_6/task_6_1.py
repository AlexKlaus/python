import urllib.request

url = 'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
logs = []

with urllib.request.urlopen(url) as response:
    for line in response:
        line = line.decode('utf-8').split(' ')
        logs.append((line[0], line[5].strip('"'), line[6]))

print(logs)
