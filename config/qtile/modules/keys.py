# vim:fileencoding=utf-8:foldmethod=marker

# This file holds keybindings for qtile excluding special cases
# These special cases include keybindings for groups, scratchpads, and mouse

from libqtile.config import Key
from libqtile.lazy import lazy


# keybind variables
## mod keys
super = "mod4"
shift = "shift"
alt = "mod1"
control = "control"

## applications
terminal = "kitty"
browser = "firefox"

# windows
window_keys = [
# {{{
    # window focus
    Key(
        [super], "h", 
        lazy.layout.left(), 
        desc="Move focus to left",
    ),
    Key(
        [super], "l", 
        lazy.layout.right(), 
        desc="Move focus to right",
    ),
    Key(
        [super], "j", 
        lazy.layout.down(), 
        desc="Move focus down",
    ),
    Key(
        [super], "k", 
        lazy.layout.up(), 
        desc="Move focus up",
    ),
    Key(
        [super], "n", 
        lazy.layout.next(), 
        desc="Move to next window",
    ),
    # window move
    Key(
        [super, shift], "h", 
        lazy.layout.shuffle_left(), 
        desc="Move window to the left",
    ),
    Key(
        [super, shift], "l", 
        lazy.layout.shuffle_right(), 
        desc="Move window to the right",
    ),
    Key(
        [super, shift], "j", 
        lazy.layout.shuffle_down(), 
        desc="Move window down",
    ),
    Key(
        [super, shift], "k", 
        lazy.layout.shuffle_up(), 
        desc="Move window up",
    ),
    # window manipulation
    Key(
        [super, control], "h", 
        lazy.layout.grow_left(), 
        desc="Grow window to the left",
    ),
    Key(
        [super, control], "l", 
        lazy.layout.grow_right(), 
        desc="Grow window to the right",
    ),
    Key(
        [super, control], "j", 
        lazy.layout.grow_down(), 
        desc="Grow window down",
    ),
    Key(
        [super, control], "k", 
        lazy.layout.grow_up(), 
        desc="Grow window up"
    ),
    Key(
        [super, control], "n", 
        lazy.layout.normalize(), 
        desc="Reset all window sizes",
    ),
    Key(
        [super, shift], "c", 
        lazy.window.kill(), 
        desc="Kill focused window",
    ),
    Key(
        [super], "f", 
        lazy.window.toggle_fullscreen(), 
        desc="Make focused window fullscreen",
    ),
    Key(
        [super], "space", 
        lazy.next_layout(), 
        desc="Change to next window",
    ),
]
# }}}

# system
system_keys = [
# {{{
    # qtile
    Key(
        [super, control], "r", 
        lazy.reload_config(), 
        desc="Reload the config",
    ),
    Key(
        [super, control], "q", 
        lazy.shutdown(), 
        desc="Shutdown Qtile",
    ),
    # system management
    Key(
        [super, control], "p", 
        lazy.spawn("xfce4-power-manager -c"), 
        desc="Launch xfce power manager",
    ),
    Key(
        [super, control], "x", 
        lazy.spawn("archlinux-logout"), 
        desc="Logout popup",
    ),
    Key(
        [super, control], "a", 
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
        [super], "r", 
        lazy.spawn("rofi -show run"), 
        desc="Launch rofi run",
    ),
    Key(
        [super, shift], "r", 
        lazy.spawn("rofi -show drun"), 
        desc="Launch rofi drun",
    ),
    # browser
    Key(
        [super], "b", 
        lazy.spawn("qutebrowser"), 
        desc="Launch qutebrowser",
    ),
    Key(
        [super, shift], "b", 
        lazy.spawn(browser), 
        desc="Launch browser",
    ),
    # terminal
    Key([super], "Return", lazy.spawn(terminal), desc="Launch terminal"),
]
# }}}
