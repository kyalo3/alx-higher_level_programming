#!/usr/bin/python3
"""a Python script that fetches"""
from urllib.request import urlopen

url = "https://alx-intranet.hbtn.io"

with urlopen(url) as response:

    x_request_head = response.getheader("X-Request-Id")
    print(x_request_head)
