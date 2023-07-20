#!/usr/bin/env bash

# rofi -show drun

(conky -c $HOME/.config/conky/qtileconky.lua) &
(conky -c $HOME/.config/conky/general.conkyrc) &
