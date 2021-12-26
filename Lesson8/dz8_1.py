import re

def email_parse(email):
    res = re.match(r'(?P<username>\w+)@(?P<domain>\w+\.\w+)',email)
    try:
        res1 = res.groupdict()
        print(res1)
    except AttributeError:
        print('ValueError: wrong email: ',email)

if __name__ == '__main__':
    email_parse()



