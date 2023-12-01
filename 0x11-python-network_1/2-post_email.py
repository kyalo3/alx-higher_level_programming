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
    data = urllib.parse.urlencode({"email": email}).encode("utf-8")

    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
