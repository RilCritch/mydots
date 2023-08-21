# vim:fileencoding=utf-8:foldmethod=marker

import os
import subprocess

from libqtile import layout, hook
from libqtile.config import Screen, ScratchPad

from modules.settings import *
 
from modules.layouts import  base_layouts, base_float_rules, floating_opts
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
        top = top_bar,
        bottom = bot_bar,
        # gaps to show conky if i want that
        # right = bar.Gap(
        #     size = 280,
        # ),
        # left = bar.Gap(
        #     size = 280,
        # ),
    ),
]

# floating layout
floating_layout = layout.Floating(base_float_rules, **floating_opts)

# hooks
# startup
@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])

# set window  property for matching in picom
@hook.subscribe.startup
def _():
    top_bar.window.window.set_property("QTILE_BAR", 1, "CARDINAL", 32)

# stuff to do after qtile has completely started
@hook.subscribe.startup_complete
def _():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/start.sh'])
    
