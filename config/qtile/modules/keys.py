# vim:fileencoding=utf-8:foldmethod=marker

# This file holds keybindings for qtile excluding special cases
# These special cases include keybindings for groups, scratchpads, and mouse
import importlib

from libqtile.config import Key
from libqtile.lazy import lazy

from modules.settings import SUPER, SHIFT, ALT, CONTROL, TERMINAL, BROWSER, EDITOR

# windows {{{
window_keys = [
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
    # window move
    Key(
        [ALT], "h", 
        lazy.layout.shuffle_left(), 
        lazy.layout.move_left(),
        desc="Move window to the left",
    ),
    Key(
        [ALT], "l", 
        lazy.layout.shuffle_right(), 
        lazy.layout.move_right(),
        desc="Move window to the right",
    ),
    Key(
        [ALT], "j", 
        lazy.layout.shuffle_down(), 
        lazy.layout.move_down(),
        desc="Move window down",
    ),
    Key(
        [ALT], "k", 
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
        lazy.layout.shrink(),
        desc="Grow window down",
    ),
    Key(
        [SUPER, CONTROL], "k", 
        lazy.layout.grow_up(), 
        lazy.layout.grow(),
        desc="Grow window up"
    ),
    Key(
        [SUPER, CONTROL], "c", 
        lazy.window.kill(), 
        desc="Kill focused window",
    ),
    Key(
        [SUPER], "minus",
        lazy.window.toggle_minimize(),
        desc="Make focused window hidden",
    ),
    Key(
        [SUPER], "equal",
        lazy.window.toggle_fullscreen(),
        desc="Make focused window fullscreen",
    ),
    Key( # rarely need
        [SUPER, CONTROL, SHIFT, ALT], "f",
        lazy.window.toggle_floating(),
        desc="Make focused window floating",
    ),
    Key(
        [SUPER], "tab",
        lazy.next_layout(),
        desc="Switch to next layout",
    ),
    # Key( # don't need
    #     [SUPER, SHIFT], "tab",
    #     lazy.prev_layout(),
    #     desc="Switch to previous layout",
    # ),
]
# }}}

# system {{{
system_keys = [
    # qtile
    # Key(
    #     [SUPER, CONTROL], "r", 
    #     lazy.reload_config(), 
    #     desc="Reload the config",
    # ),
    # Key(
    #     [SUPER, CONTROL], "x", 
    #     lazy.spawn("/home/rc/mydots/scripts/rofiscripts/powermenu.sh"),
    #     desc="Launch logout",
    # ),
    # Key(
    #     [SUPER, SHIFT], "c", 
    #     lazy.spawn("/home/rc/mydots/scripts/rofiscripts/clipboard.sh"),
    #     desc="View clipboard history",
    # ),
    # Key(
    #     [SUPER, SHIFT], "s", 
    #     lazy.spawn("/home/rc/mydots/scripts/rofiscripts/sysopts-qtile.sh"),
    #     desc="Select system options",
    # ),
]
# }}}

# applications {{{
app_keys = [
    # rofi
    Key(
        [SUPER], "r",
        lazy.spawn("rofi -modes 'run,drun' -show drun"),
        desc="Launch rofi",
    ),
    # browser
    Key(
        [SUPER], "w",
        lazy.spawn(BROWSER),
        desc="Launch browser",
    ),
    # terminal
    Key(
        [SUPER],
        "Return",
        lazy.spawn(TERMINAL),
        desc="Launch terminal"
    ),
    Key(
        [SUPER], "e",
        lazy.spawn(EDITOR),
        desc="Launch editor"
    ),
]
# }}}
