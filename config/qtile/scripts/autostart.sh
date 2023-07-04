#!/usr/bin/env bash

## Qtile startup script ##########################################################
#
## Inspired by arco linux awesome startup
#
## Author: Ril Critch
#
## Updated: 4/16/2023
#
##################################################################################

function run {
  if ! pgrep -x $(basename $1 | head -c 15) 1>/dev/null;
  then
    $@&
  fi
}

# source /home/rc/scripts/

## Startup applications ########

# arcolinux ###########

# run dex $HOME/.config/autostart/arcolinux-welcome-app.desktop

#######################

# systray #############

run nm-applet
run pamac-tray
# run volumeicon
# run blueberry-tray

#######################

#######################

# utility #############

run xfce4-power-manager
run xbindkeys
run /usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1
# run /home/rc/Documents/my_scripts/displaysetting.sh
# run /home/rc/Documents/my_scripts/appimagehandler.sh -- Need to fix so it waits until the file is downloaded fully
# run clipmenud

#######################

# look and feel #######
run picom --experimental-backends --config /home/rc/.config/qtile/specconfigs/picom.conf &
run nitrogen --restore &
# run conky -c /home/rc/.config/awesome/conky/systemoverview.config
run caffeine -a &

#######################

# applications ########
# kitty -T "Welcome" -e cxxmatrix --frame-rate 20 -c black --no-diffuse --preserve-background -m "Welcome RC" -s banner
# kitty -T "Welcome" -e cxxmatrix --frame-rate 40 -c black --no-diffuse --preserve-background -m "Welcome RC"
# rofi -show drun
# kitty --hold -e termtitle "Hello RilCritch" yellow whiteL blue

#######################

################################
