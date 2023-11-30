 #!/bin/bash

url=$1

curl -sI 'url' | grep -i 'content-length' | awk '{print $2}' | tr -d '\r'
