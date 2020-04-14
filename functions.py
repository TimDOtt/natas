#!/usr/bin/env python3
import requests 
def sessionID():
    while True:
        r = requests.post(url, auth=(username, password), data=data)
        for c in r.cookies:
            a = str(c.value)
            print(a)