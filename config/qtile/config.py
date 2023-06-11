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

from modules.keys import window_keys, system_keys, app_keys, super, shift, alt, control, terminal, browser
from modules.layouts import layout_theme, base_layouts

# keybindings 
keys = []
keys.extend(window_keys)
keys.extend(system_keys)
keys.extend(app_keys)
    
# layouts
layouts = base_layouts

# mouse bindings
# Drag floating layouts.
mouse = [
    Drag([super], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([super], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([super], "Button2", lazy.window.bring_to_front()),
    ]

## groups/workspaces {{{

# Setting up group names, labels, and default layouts
# groups = [Group(i) for i in "123456789"]
groups = []

group_names = ["1", # 1 - misc stuff
               "2", # 2 - misc stuff
               "3", # 3 - misc stuff
               "4", # 4 - browser 
               "5", # 5 - wm config
               "6", # 6 - nvim config
               "7", # 7 - coding
               "8", # 8 - music
               "9"] # 9 - discord

group_labels = ["󰾟  1", # 1 - misc stuff 
                "󰾟  2", # 2 - misc stuff
                "󰾟  3", # 3 - misc stuff
                "󰾔  4", # 4 - browser  
                "󰵆  5", # 5 - wm config
                "󰏬  6", # 6 - nvim config
                "󰈚  7", # 7 - coding
                "󰋌  8", # 8 - music
                "󰬋  9"] # 9 - discord

group_layouts = ["Columns", # 1 - misc stuff 
                 "Columns", # 2 - misc stuff
                 "Columns", # 3 - misc stuff
                 "Columns", # 4 - browser 
                 "Columns", # 5 - qtile config
                 "Columns", # 6 - nvim config
                 "Columns", # 7 - coding
                 "Columns", # 8 - music
                 "Columns"] # 9 - discord

# adding group names, labels, and layouts to group object
for i in range(len(group_names)):
    groups.append(
        Group(
            name = group_names[i],
            layout = group_layouts[i].lower(),
            label = group_labels[i],
        )
    )

# key bindings for groups
for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [super],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
                ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [super, shift],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
                ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
            ]
        )

# }}}

## Scratchpads {{{
# Sratchpad layout
# scratchpad_layout = {
#         "width": 0.8,
#         "height": 0.8,
#         "x": 0.1,
#         "y": 0.1,
#         "opacity": 1
#     }

# Scratchpads 
groups.append(ScratchPad("scratchpad", [
    DropDown("term", 
             terminal + " --class=scratch", 
             width = 0.8, 
             height = 0.8, 
             x = 0.1, 
             y = 0.1),
    DropDown("qtile keybindings", 
             terminal + " --class=scratch --hold -e /home/rc/mydots/scripts/qtilekeys", 
             width = 0.8, 
             height = 0.8, 
             x = 0.1, 
             y = 0.1),
    # DropDown("qute", 
    #          # lazy.spawn("qutebrowser qute://help/img/cheatsheet-big.png"), 
    #          ["qutebrowser"], 
    #          width = 0.8, 
    #          height = 0.8, 
    #          x = 0.1, 
    #          y = 0.1),
    ]))

# Scratchpad keybindings
keys.extend( 
    [
        Key([super, shift], 'f',
            lazy.group['scratchpad'].dropdown_toggle('term'),
            desc="Launch terminal scratchpad",
            ),
        Key([super, shift], 'q',
            lazy.group['scratchpad'].dropdown_toggle('qtile keybindings'),
            desc="Launch qtile keybindings",
            ),
        # Key([super, shift], 't', -- need to figure out issue
        #     lazy.group['scratchpad'].dropdown_toggle('qute'),
        #     desc="Launch qutebrowser",
        #     ),
    ])
# }}}

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
floating_layout = layout.Floating(
    float_rules = [
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class="floating"),
        # Match(wm_class="qutebrowser"),
        ],
    **layout_theme,
)
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
