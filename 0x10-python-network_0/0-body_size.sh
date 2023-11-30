#!/bin/bash
# bash script that sends a request to a url and displays the size of body
curl -s "$1" | wc -c
