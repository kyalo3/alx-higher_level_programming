 #!/bin/bash

if [ $# -eq 0 ];
then echo 'Usage: $0 <URL>'
     exit 1
fi

url=$1
params={ 'email=test@gmail.com', 'subject=I will always be here for PLD' }

response=$(curl -s -X POST -d 'params' 'url')
echo '$response!'
