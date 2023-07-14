#!/usr/bin/env bash


# title
figlet -k -f shadow "Reminders" | clr blue

# reminders
userfile="$HOME/documents/testing/$USER-reminders.txt"
\cat -n $userfile | clr green
