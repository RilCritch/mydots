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

## qtile bar {{{
widget_defaults = dict(
    # font="sans",
    font="JetBrainsMono Nerd Font",
    fontsize=14,
    padding=4,
    foreground='#edeff0'
    )

extension_defaults = widget_defaults.copy()

sep_theme = {
        "linewidth": 1,
        "padding": 10,
        "foreground": '#505253'
    }

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Volume(
                    scroll_delay=0,
                    foreground='#edeff0',
                    ),
                widget.Sep(**sep_theme),
                widget.Prompt(),
                widget.WindowName(padding=6),
                widget.Sep(**sep_theme),
                widget.GroupBox(
                    highlight_method='line',
                    hide_unused=True,
                    # highlight_color=['#0c0e0f', 
                    #                  '#505253',
                    #                  '#505253',
                    #                  '#0c0e0f'],
                    highlight_color='#343637',
                    # this_current_screen_border='#ecd28b',
                    inactive='#505253',
                    active='#edeff0',
                    # fontshadow='#0c0e0f',
                    font="JetBrainsMono Nerd Font Bold",
                    block_highlight_text_color='#ecd28b',
                    borderwidth=0,
                    # margin=5,
                    padding=1,
                    fontsize=16,
                    ),
                widget.Sep(**sep_theme),
                widget.Spacer(),
                widget.Sep(**sep_theme),
                widget.Clock(format="%I:%M"),
            ],
            30,
            background='#0c0e0f',
            opacity=0.90,
            border_width=[0, 0, 2, 0], 
            border_color='#ecd28b'
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),

        bottom=bar.Bar(
            [
                widget.Systray(icon_size=15),    
                widget.Spacer(),
                # widget.CapsNumLockIndicator(),
                widget.CurrentLayoutIcon(),
            ],
            20,
            background='#0c0e0f',
            opacity=0.90,
        ),
    ),
]
# }}}

# floating layout {{{
floating_layout = layout.Floating(base_float_rules, **layout_theme)
# floating_layout = layout.Floating(
#     float_rules = [
#         # Run the utility of `xprop` to see the wm class and name of an X client.
#         *layout.Floating.default_float_rules,
#         Match(wm_class="confirmreset"),  # gitk
#         Match(wm_class="makebranch"),  # gitk
#         Match(wm_class="maketag"),  # gitk
#         Match(wm_class="ssh-askpass"),  # ssh-askpass
#         Match(title="branchdialog"),  # gitk
#         Match(title="pinentry"),  # GPG key password entry
#         # Match(wm_class="qutebrowser"),
#         ],
#     **layout_theme,
# )
# }}}

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
