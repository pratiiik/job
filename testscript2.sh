#!/bin/bash

if [ -f  $1 ]; then
 echo "$1 is a file"
elif [ -d  $1 ]; then
 echo "$1 is a directory"

else
 echo "$1 is neither a file nor a directory"
 exit 1
fi
exit 0

