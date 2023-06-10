# vim:fileencoding=utf-8:foldmethod=marker

## library imports {{{

import importlib
import os
import re
import socket
import subprocess
from typing import List

from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy
# from libqtile.utils import guess_terminal

# }}}

## general keybindings {{{

mod = "mod4"
terminal = "kitty"

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "n", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Make focused window fullscreen"),
    
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod, "control"], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "space", lazy.next_layout(), desc="Toggle between layouts"),

    # Launch applications
    ## Rofi
    Key([mod], "r", lazy.spawn("rofi -show run"), desc="Launch rofi run"),
    Key([mod, "shift"], "r", lazy.spawn("rofi -show drun"), desc="Launch rofi drun"),
    ## Firefox
    Key([mod, "shift"], "b", lazy.spawn("firefox"), desc="Launch firefox"),
    ## Terminal
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    ## Power manager
    Key([mod, 'shift'], "p", lazy.spawn("xfce4-power-manager -c"), desc="Launch xfce power manager"),

    # System info
    # Keybindings - the command works now I just need to figure out how to spawn it in a floating window
    # Key([mod, "shift"], "q", 
    #     lazy.spawn('kitty --class=floating --hold -e /home/rc/mydots/scripts/qtilekeys'
    #                ), 
    #     desc="Show keybindings"
    #     ),
    ]

# }}}

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
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
                ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
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
             "kitty --class=scratch", 
             width = 0.8, 
             height = 0.8, 
             x = 0.1, 
             y = 0.1),
    DropDown("qtile keybindings", 
             "kitty --class=scratch --hold -e /home/rc/mydots/scripts/qtilekeys", 
             width = 0.8, 
             height = 0.8, 
             x = 0.1, 
             y = 0.1),
    DropDown("qute keybindings", 
             # lazy.spawn("qutebrowser qute://help/img/cheatsheet-big.png"), 
             ["/usr/bin/qutebrowser"], 
             width = 0.8, 
             height = 0.8, 
             x = 0.1, 
             y = 0.1),
    ]))

# Scratchpad keybindings
keys.extend( 
    [
        Key([mod, 'shift'], 'f',
            lazy.group['scratchpad'].dropdown_toggle('term'),
            desc="Launch terminal scratchpad",
            ),
        Key([mod, 'shift'], 'q',
            lazy.group['scratchpad'].dropdown_toggle('qtile keybindings'),
            desc="Launch qtile keybindings",
            ),
        Key([mod, 'shift'], 't',
            lazy.group['scratchpad'].dropdown_toggle('qute keybindings'),
            desc="Launch qutebrowser keybindings",
            ),
    ])

# }}}
    
## layouts {{{

layout_theme = {
    "margin": 12,
    "border_width": 3,
    "border_focus": "#ecd28b",
    "border_normal": "#0c0e0f"
    }

layouts = [
    layout.Columns(**layout_theme), # favorite
    layout.Max(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    ]

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

## mouse bindings {{{

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
    ]

# }}}

## startup {{{

# Startup stuff -- need to move to a startup script
# @hook.subscribe.startup_once
# def autostart():
#     qtile.cmd_spawn('nitrogen --restore')
#     qtile.cmd_spawn('nm-applet')
#     qtile.cmd_spawn('pamac-tray')
#     qtile.cmd_spawn('xbindkeys')
@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])

# }}}

## floating layout {{{

floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class="floating"),
        ],
    **layout_theme,
    )

# }}}

## configuration variables {{{

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

# }}}
