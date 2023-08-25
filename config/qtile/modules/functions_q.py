# vim:fileencoding=utf-8:foldmethod=marker

import os

from libqtile.lazy import lazy


# volume control using amixer -- must have amixer on system
@lazy.function
def mute_toggle(qtile): # pyright: ignore
    os.system("amixer set Master toggle")

@lazy.function
def vol_inc(qtile): # pyright: ignore
    os.system("amixer set Master 1%+")

@lazy.function
def vol_dec(qtile): # pyright: ignore
    os.system("amixer set Master 1%-")
