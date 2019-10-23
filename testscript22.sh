#!/bin/bash
count=1
dir_count=0
file_count=0
find /home/pratik/DIR_scripts | while read line; do
  echo  
  echo "content $count"
  var=$(echo $line | cut -d/ -f5)
  echo $var
  if [ -f $var ];
  then
  file_count=$(( $file_count + 1 ))
  echo "above content is a file"
  echo $file_count
  elif [ -d $var ];
  then
  dir_count=$(( $dir_count+1 ))
  echo "above content is a directory"
  echo $dir_count
  else
  echo "something unexpected came in"
  fi
  count=$(( $count+1 ))
  
done
echo "Number of files: $file_count and Number of directory: $dir_count"

