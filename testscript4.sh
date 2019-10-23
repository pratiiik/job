#!/bin/bash

USAGE() {
  echo "Enter an argument"
  echo "USAGE: $0"
 }

IS_FILE_EXIST() { 
  
  local file="$1"

# In the below line if the statement is true inside [[ ]] it will be 1
# then  execution will go to return 1 rather than going to return 0.
# ********************************************************************

  [[ -f "$file" ]] && return 0 || return 1

 }

[[ $# -eq 0 ]] && USAGE

if ( IS_FILE_EXIST "$1" )
then
     echo "file $1 exists."
else 
     echo "file $1 does not exist."
fi

exit 0

