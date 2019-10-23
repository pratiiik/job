#!/bin/bash

echo "System check is about to happen"

echo "Ports running are : "
echo
#netstat -nltp | awk 'NR>3 && NR<10'
netstat -nltp

me=`who | awk '{print $1}'`
online_time=`who | awk '{print $4}'`
echo 
echo "$me is online since $online_time"

#speed=`ping -c10 -w10 192.168.0.1`

result=`ping -c10 -w10 192.168.0.1 | grep avg | awk '{print $4}' | cut -d'/' -f2`
#result1=`ping -c10 -w10 192.168.0.1 | grep avg | awk '{print $4}'`

echo
echo "avg speed is : $result ms"
echo
#result="3.98"
#res=$(($result + 0))
if (( `bc <<< "$result > 4"` ));
then
 echo "starting network-manager"
 sleep 2s
 service network-manager restart
 sleep 3s
 echo "started, check now..."
else
 echo "speed is ok"
fi
