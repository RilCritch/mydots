#!/usr/bin/env bash

# here I am testing different fundtionality I want the the script to have
# eventually I would like to set flags, so you can do different things without interactive propmt

# depencies: clr(my script)


# user reminders file name file
userfile="$HOME/documents/testing/$USER-reminders.txt"


# creating a file that holds the reminders
# func form

reminders_file_check () {

if [ ! -f $userfile ]; then
  echo "No reminders found for user '$USER'" | clr yellow
  
  echo -n "creating file at " 
  echo "'$userfile'" | clr blue

  touch $userfile
else
  echo "Reminders found for user '$USER'" | clr green
  # print reminders?
fi
}

reminders_file_check


# echo
# # retrieve reminders as an array if it exsists
# if [ -f $userfile ]; then
#   readarray -t reminders_array < "$userfile"
#   echo "Reminders loaded successfully" | clr green
#   
# else
#   echo "Error... failed to load reminders" | clr red
# fi


# adding reminders to file
add_reminders () {

echo "Adding reminders: Each line is a single reminder (type 'exit' to quit)"

while true; do
  # echo -n "Reminder to add: " # eventually add reminder number or something
  read -p "New entry: " choice

  if [ "$choice" = "exit" ]; then
    echo "Exiting..." | clr yellow
    break
  fi

  if [ -z "$choice" ]; then
    echo "Error... no input. To stop adding reminders type 'exit'" | clr red
    continue
  fi
  
  echo "$choice" >> $userfile
done

}

echo
add_reminders


# print out reminders
# method one - no numbers
# for reminder in "${reminders_array[@]}"; do
#   echo "Reminder: $reminder"
# done

# method two - numbers *** better option -- manually needs array
# print_reminders () {
# for ((i=0; i<${#reminders_array[@]}; i++)); do
#   reminder_number=$((i+1))
#   reminder="${reminders_array[i]}"
#
#   echo "$reminder_number. $reminder" | clr green
# done
# }

# menthod thee - nummbers *** best option -- with cat doesnt need array
print_reminders () {

  # header text?
  if [ ! -z $1 ]; then
    echo "$1" | clr blue
  fi

  \cat -n $userfile | clr green

}

echo
print_reminders "Reminders"

# removing reminders
# by number - for interactive prompt
echo


remove_reminders () { # need to figure out good ux for this

echo "Remove a reminder: Enter reminder number to remove (type 'exit' to quit)"

while true; do
  print_reminders

  read -p "Number to remove: " choice

  if [ "$choice" = "exit" ]; then
    echo "Exiting..." | clr yellow
    break
  fi

  if [ -z "$choice" ]; then
    echo "Error... no input. To stop removing reminders type 'exit'" | clr red
    continue
  fi

  if [[ ! $choice =~ ^[0-9]+$ ]]; then
    echo "Error... please enter a positive integer" | clr red 
    continue
  fi

  line_count=$(wc -l < $userfile)
  if [ "$choice" -gt "$line_count" ]; then
    echo "Error... this reminder does not exsist" | clr red
    continue
  fi
  
  sed -i "${choice}d" $userfile
done

}

remove_reminders

# by reminder - fzf method?
