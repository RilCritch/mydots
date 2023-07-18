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

run nm-applet &
run pamac-tray &
run volumeicon &
run blueberry-tray &

#######################

#######################

# utility #############

run xfce4-power-manager &
run /usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1
clipster -d &
# run clipmenud

#######################

# look and feel #######
run nitrogen --restore &
run picom --experimental-backends --config /home/rc/.config/qtile/specconfigs/picom.conf &
/usr/lib/xfce4/notifyd/xfce4-notifyd &
# run caffeine -a &

#######################
