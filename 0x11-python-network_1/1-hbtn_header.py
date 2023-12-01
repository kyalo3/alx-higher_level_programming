#!/usr/bin/python3
"""a Python script that fetches"""
import urllib.request
import sys

url = "https://alx-intranet.hbtn.io"

with urlopen(url) as response:

    x_request_id = response.getheader("X-Request-Id")
    print(x_request_id)
