#!/bin/bash

trap "cat $1; exit 0" 0 2 15

echo "this script will print a number 10 times"

var=10

while (( var > 0 ))
do

  echo $var
  sleep 3
  (( var --))
done
exit 0

