 #!/bin/bash

if [ $# -eq 0 ];
then echo 'Usage: $0 <URL>'
     exit 1
fi

url=$1

size=$(curl -sI 'url' | grep )
echo 'Size of the response body: ${size} bytes'
