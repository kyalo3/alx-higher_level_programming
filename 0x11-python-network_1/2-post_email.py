#!/usr/bin/python3
"""
Python script that takes in a URL and an
email, sends a POST request to the passed URL
with the email as a parameter"""

import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    """ get URL and email from command line arguments"""
    url = sys.argv[1]
    email = sys.argv[2]

    """encode the email as a URL parameter"""
    data = urllib.parse.urlencode({"email": sys.argv[2]}).encode("ascii")

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
