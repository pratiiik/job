#!/bin/bash

echo "printing memory usage"
echo "_______________"
free -h | awk '/Mem:/ {print $1 " " $3 "/" $2}'
echo
echo "printing Temp stats"
echo "_______________"
sensors | awk '/temp1/ {print $1 " " $2}'
echo
echo "printing top 10 memory hogging processes"
echo "_______________"
ps axch -o cmd:11,%mem --sort=-%mem | head
echo
echo "printing top 10 cpu hogging processes"
echo "______________"
ps axch -o cmd:11,%cpu --sort=-%cpu | head
 
