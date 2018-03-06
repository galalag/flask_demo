#!/usr/local/bin/python3

import requests

r = requests.post("http://127.0.0.1:8084/demo", json={"message": "hello"})
print('response', r)
print('status_code', r.status_code)
print('json', r.json())
            
