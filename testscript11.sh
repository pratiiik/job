#!/bin/bash

echo "what i am going to do?"
name=$1
set `who`
#in the above line who will be used as a command and its output will be dire
#cted as input for set. 
mv $name $name.$1

