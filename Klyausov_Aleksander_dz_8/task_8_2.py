import re
import urllib.request


def parse_logs(log):
    re_log = re.compile(r'(?P<remote_addr>((\w+[:.])|[:]){3,7}\w+) - - \['  # ip4 и ip6
                        r'(?P<request_datetime>[\W\w]+)] "'
                        r'(?P<request_type>\w+) '
                        r'(?P<requested_resource>(/\w+)+) [\W\w]+" '
                        r'(?P<response_code>\d+) '
                        r'(?P<response_size>\d+)')
    # assert re_log.match(log), f'Ошибка в строке {log}'  # Проверка шаблона
    return tuple(re_log.match(log).groupdict().values())


url = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'


with urllib.request.urlopen(url) as f:
    for line in f:
        print(parse_logs(line.decode('utf-8')))
