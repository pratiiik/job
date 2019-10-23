i#!/bin/bash

PS3="please enter the number from above list: "
select var in foo bar cool sun
do
#echo -e "values are $var \c"
case $var in
foo)ls;;
bar)pwd;;
cool)$HOME;;
sun)exit;;
*)echo "Error"
esac

done

