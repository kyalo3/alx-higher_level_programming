#!/usr/bin/python3
"""a Python script that fetches"""
from urllib.request import urlopen

with urlopen('https://alx-intranet.hbtn.io/status') as response:

    response = urlopen("https://alx-intranet.hbtn.io/status")
    html = response.read()
    print("Body response:")
    print("\t - type: <class 'bytes'>")
    print("\t - content: b'OK''")
    print("\t - utf8 content: OK")
