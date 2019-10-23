
for file in `ls`
do
  if [[ -s $file ]];then

     printf "$file is non empty\n"
    
     grep "echo" $file
  else
     printf "$file is empty\n"

     printf "Deleting this empty file\n"

     rm -rf $file

  fi

done
exit 0
