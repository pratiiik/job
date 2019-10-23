#!/bin/bash

PS3="SELECT FROM ABOVE LIST: "
select drinks in cofee tea juice wine rum vodaka
do
   case $drinks in
        cofee|tea) echo "go to your home kid";;
       
        juice) echo "go to market kid";;
     
        wine|rum|vodaka) echo "go to ur mom kid";;
        
        *)echo "go to ur gf kid"      
 
   esac

done

       
