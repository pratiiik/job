#!/bin/bash

USG_ERR=7
max_two ( ) {
if [ "$1" -eq "$2" ] ; then
echo 'Equal'
exit 0
elif [ "$1" -gt "$2" ] ; then
echo $1
else
echo $2
fi
}
err_str ( ) {
echo "Usage: $0 <number1>  <number2>"
exit $USG_ERR
}
NUM_1=$1
NUM_2=$2
#x
if [ $# -ne 2 ] ; then
err_str
elif [ `expr $NUM_1 : '[0-9]*'` -eq ${#NUM_1} ] ; then
if [ `expr $NUM_2 : '[0-9]*'` -eq ${#NUM_2} ] ; then  
max_two $NUM_1 $NUM_2
else
err_str
fi
else
err_str
fi
exit 0
