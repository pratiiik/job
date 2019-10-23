


echo -e "print the filename \c"
read file

if [[ -f $file ]]; then
     echo "$file exists"
     ls -l $file && less $file

else 
     :
     
fi


