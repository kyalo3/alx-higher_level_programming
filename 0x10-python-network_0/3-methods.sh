#!/bin/bash
# bash script that takes in a URL and displays all methods
methods=("GET" "HEAD" "POST" "PUT" "DELETE")
for method in "${methods[@]}"; do
   
curl -X OPTIONS HEAD PUT "$1", "$2", "$3"
