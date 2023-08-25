# vim:fileencoding=utf-8:foldmethod=marker

from libqtile.config import Drag, Click
from libqtile.lazy import lazy

from modules.settings import SUPER, SHIFT
from modules.functions_q import mute_toggle, vol_inc, vol_dec


mouse_float = [
    # floating window control
    Drag(
        [SUPER], "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [SUPER], "Button3",
        lazy.window.set_size_floating(),
        start=lazy.window.get_size(),
    ),

    # volume control
    Click(
        [SUPER, SHIFT], "Button2",
        mute_toggle(),
    ),
    Click(
        [SUPER, SHIFT], "Button4",
        vol_inc(),
    ),
    Click(
        [SUPER, SHIFT], "Button5",
        vol_dec(),
    ),

    # groups
    Click(
        [SUPER, SHIFT], "Button6",
        lazy.screen.prev_group(),
    ),
    Click(
        [SUPER, SHIFT], "Button7",
        lazy.screen.next_group(),
    ),
]
