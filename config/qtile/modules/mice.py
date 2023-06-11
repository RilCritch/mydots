# vim:fileencoding=utf-8:foldmethod=marker

from libqtile.config import Drag, Click
from libqtile.lazy import lazy

from settings import SUPER

mouse_float = [
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
    Click(
        [SUPER], "Button2", 
        lazy.window.bring_to_front(),
    ),
]
