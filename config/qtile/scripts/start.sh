#!/usr/bin/env bash

# rofi -show drun

(conky -c $HOME/.config/conky/qtile.conkyrc) &
(conky -c $HOME/.config/conky/general.conkyrc) &
