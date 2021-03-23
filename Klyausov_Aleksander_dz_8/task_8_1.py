import re


def email_parse(email_address):
    re_email = re.compile(r'(?P<username>\w+)@(?P<domain>\w+\.\w+)')
    if re_email.match(email_address):
        return re_email.match(email_address).groupdict()
    else:
        msg = f'wrong email: {email_address}'
        raise ValueError(msg)


print(email_parse('krounix@gmail.com'))
