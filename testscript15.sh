clear
printf "Enter number\n"
read num
n=$num
rev=0
while [[ $num -ne 0 ]]
do  
  rem=`expr $num % 10`
  
  rev=`expr $rev \* 10 + $rem`
 
  num=`expr $num / 10`


done
if [[ $n -eq $rev ]]
then
   printf "$n is a pallandrom\n"
fi

printf "Reverse number is $rev\n"

exit 0

