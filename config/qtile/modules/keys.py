# vim:fileencoding=utf-8:foldmethod=marker

# This file holds keybindings for qtile excluding special cases
# These special cases include keybindings for groups, scratchpads, and mouse
import importlib

from libqtile.config import Key
from libqtile.lazy import lazy

from settings import SUPER, SHIFT, ALT, CONTROL, TERMINAL, BROWSER

window_keys = [
# {{{
    # window focus
    Key(
        [SUPER], "h", 
        lazy.layout.left(), 
        desc="Move focus to left",
    ),
    Key(
        [SUPER], "l", 
        lazy.layout.right(), 
        desc="Move focus to right",
    ),
    Key(
        [SUPER], "j", 
        lazy.layout.down(), 
        desc="Move focus down",
    ),
    Key(
        [SUPER], "k", 
        lazy.layout.up(), 
        desc="Move focus up",
    ),
    Key(
        [SUPER], "n", 
        lazy.layout.next(), 
        desc="Move to next window",
    ),
    Key(
        [SUPER], "m", 
        lazy.layout.previous(), 
        desc="Move to previous window",
    ),
    # window move
    Key(
        [SUPER, SHIFT], "h", 
        lazy.layout.shuffle_left(), 
        lazy.layout.move_left(),
        desc="Move window to the left",
    ),
    Key(
        [SUPER, SHIFT], "l", 
        lazy.layout.shuffle_right(), 
        lazy.layout.move_right(),
        desc="Move window to the right",
    ),
    Key(
        [SUPER, SHIFT], "j", 
        lazy.layout.shuffle_down(), 
        lazy.layout.move_down(),
        desc="Move window down",
    ),
    Key(
        [SUPER, SHIFT], "k", 
        lazy.layout.shuffle_up(), 
        lazy.layout.move_up(),
        desc="Move window up",
    ),
    # window manipulation
    Key(
        [SUPER, CONTROL], "h", 
        lazy.layout.grow_left(), 
        desc="Grow window to the left",
    ),
    Key(
        [SUPER, CONTROL], "l", 
        lazy.layout.grow_right(), 
        desc="Grow window to the right",
    ),
    Key(
        [SUPER, CONTROL], "j", 
        lazy.layout.grow_down(), 
        desc="Grow window down",
    ),
    Key(
        [SUPER, CONTROL], "k", 
        lazy.layout.grow_up(), 
        desc="Grow window up"
    ),
    Key(
        [SUPER, CONTROL], "n", 
        lazy.layout.normalize(), 
        desc="Reset all window sizes",
    ),
    Key(
        [SUPER, SHIFT], "c", 
        lazy.window.kill(), 
        desc="Kill focused window",
    ),
    Key(
        [SUPER, CONTROL], "f", 
        lazy.window.toggle_fullscreen(), 
        desc="Make focused window fullscreen",
    ),
    Key(
        [SUPER], "f", 
        lazy.window.toggle_floating(), 
        desc="Make focused window floating",
    ),
    Key(
        [SUPER], "space", 
        lazy.next_layout(), 
        desc="Switch to next layout",
    ),
    Key(
        [SUPER, SHIFT], "space", 
        lazy.prev_layout(), 
        desc="Switch to previous layout",
    ),
]
# }}}

# system
system_keys = [
# {{{
    # qtile
    Key(
        [SUPER, CONTROL], "r", 
        lazy.reload_config(), 
        desc="Reload the config",
    ),
    Key(
        [SUPER, CONTROL], "q", 
        lazy.shutdown(), 
        desc="Shutdown qtile",
    ),
    # system management
    Key(
        [SUPER, CONTROL], "p", 
        lazy.spawn("xfce4-power-manager -c"), 
        desc="Launch xfce power manager",
    ),
    Key(
        [SUPER, CONTROL], "x", 
        lazy.spawn("archlinux-logout"), 
        desc="Logout popup",
    ),
    Key(
        [SUPER, CONTROL], "a", 
        lazy.spawn("archlinux-tweak-tool"), 
        desc="Logout popup",
    ),
]
# }}}

# applications
app_keys = [
# {{{    
    # rofi
    Key(
        [SUPER], "r", 
        lazy.spawn("rofi -show run"), 
        desc="Launch rofi run",
    ),
    Key(
        [SUPER, SHIFT], "r", 
        lazy.spawn("rofi -show drun"), 
        desc="Launch rofi drun",
    ),
    # browser
    Key(
        [SUPER], "b", 
        lazy.spawn("qutebrowser"), 
        desc="Launch qutebrowser",
    ),
    Key(
        [SUPER, SHIFT], "b", 
        lazy.spawn(BROWSER), 
        desc="Launch browser",
    ),
    # terminal
    Key([SUPER], "Return", lazy.spawn(TERMINAL), desc="Launch terminal"),
]
# }}}
