#!/bin/sh

echo $1 $2 $3
IFS=""
echo "$@"
echo "$*"
unset IFS
echo "$@"
echo "prameter list was $*"
echo "the program $0 is now running"
echo "first parameter is $1"
echo "second parameter is $2"
echo "third parameter is $3"
echo "user's home directory is $HOME"
echo "please select new input  "
read new
echo "new input is $new"
echo "scrpt is complete"
exit 0



