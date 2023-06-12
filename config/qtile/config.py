# vim:fileencoding=utf-8:foldmethod=marker

import importlib
import os
import re
import socket
import subprocess
from typing import List

from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy

from modules.layouts import layout_theme, base_layouts, base_float_rules

from modules.settings import SUPER, SHIFT, ALT, CONTROL
from modules.settings import TERMINAL, BROWSER

from modules.keys import window_keys, system_keys, app_keys
from modules.groups_q import main_groups, group_keys
from modules.scratchpads_q import spads, spad_keys
from modules.mice import mouse_float
from modules.bars import top_bar, bot_bar, widget_defaults

# main keybindings 
keys = []
keys.extend(window_keys)
keys.extend(system_keys)
keys.extend(app_keys)
    
# main layouts
layouts = base_layouts

# mouse bindings
mouse = []
mouse.extend(mouse_float)

# main groups
groups = []
groups.extend(main_groups)
keys.extend(group_keys)

# Scratchpads 
groups.append(ScratchPad("scratchpad", spads))
keys.extend(spad_keys)

# bar
extension_defaults = widget_defaults.copy()
screens = [
    Screen(
        top=top_bar,
        bottom=bot_bar,
    ),
]

# floating layout
floating_layout = layout.Floating(base_float_rules, **layout_theme)

# startup
@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])

# configuration options
dgroups_key_binder = None
dgroups_app_rules = []  # type: list
# follow_mouse_focus = True -- figure out a way to toggle between settings
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
