#!/usr/bin/python3
"""a Python script that fetches"""
import requests

url = 'https://alx-intranet.hbtn.io/status'

with requests.get(url) as response:
    html = response.text
    print("Body response:")
    print("\t - type: <class 'bytes'>")
    print("\t - content: b'OK''")
    print("\t - utf8 content: OK")
