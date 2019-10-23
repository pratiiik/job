#!/bin/bash
echo "total number of files and directories are=$#"
a=30
b=15
echo the sum is `expr $a + $b`
echo the sub is `expr $a - $b`
echo the div is `expr $a / $b`
echo the mul is `expr $a \* $b`
echo the remainder is `expr $a % $b`
a=30.45
b=15.20
c=`echo $a + $b | bc`
d=`echo $a - $b | bc`
e=`echo $a \* $b | bc`
f=`echo $a  / $b | bc`
g=`echo $a % $b | bc`
echo the sum is $c
echo the sub is $d
echo the mul is $e
echo the div is $f
echo the remainder is $g


