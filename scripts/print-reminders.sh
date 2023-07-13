#!/usr/bin/env bash


# title
figlet -f small "Reminders" | clr blue

# reminders
userfile="$HOME/documents/testing/$USER-reminders.txt"
\cat -n $userfile | clr green
