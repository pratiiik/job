
if [[ $(whoami) != "root" ]];
then
   printf "You are not root be careful.\n"
   echo -e "Your present working directory is: $PWD"

fi

name=("Naman" "Sudha" "Pushpa")
name[1]="Naman"
name[0]="Sudha"
count=0

for MY_RAND in ${name[*]};
do
  (( count++ ))
  printf "MERI RANDI NUMBER $count HAI $MY_RAND\n"
  if [[ $MY_RAND = "Sudha" ]]
  then
      printf "*********************************\n
       MEri MAst CHinal RAnd Hai sali $MY_RAND.\n
      Kya mst gand hai meri chinal ki?\n
      Ahhhhhhhhhhh,Sali rand $MY_RAND.\n"
      printf "*********************************\n"
  fi
  
done


