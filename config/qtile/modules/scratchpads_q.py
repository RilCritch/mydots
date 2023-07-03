# vim:fileencoding=utf-8:foldmethod=marker

from libqtile.config import DropDown, Key, Match
from libqtile.lazy import lazy

from modules.settings import SUPER, SHIFT, TERMINAL
    
from modules.confutils import window_info


# functions for generating dropdown -- code from: https://github.com/ViperX7/qtile_config/blob/main/q_scratchpads.py
def scratchgen(name, spawn, h, w, x=None, y=None, autohide=False, res="", opacity=1):
    # center everything by default
    if x is None:
        x = x if x else (1 - w) / 2
    if y is None:
        y = y if y else (1 - h) / 2
    # y = y - 0.015
    if res:
        spad = DropDown(
            name,
            spawn,
            match=Match(wm_class=res),
            width=w,
            height=h,
            x=x,
            y=y,
            opacity=opacity,
            on_focus_lost_hide=autohide,
        )
    else:
        spad = DropDown(
            name,
            spawn,
            width=w,
            height=h,
            x=x,
            y=y,
            opacity=opacity,
            on_focus_lost_hide=autohide,
        )
    return spad

# default layout?
# scratchpad_layout = {
#         "width": 0.8,
#         "height": 0.8,
#         "x": 0.1,
#         "y": 0.1,
#         "opacity": 1
#     }

# list of dropdowns
SCRATCHTERM = TERMINAL + " --class=scratchterm"
spads = [
    scratchgen( # basic terminal
        "term",
        SCRATCHTERM,
        0.985,
        window_info.calculate_size_percent(1350),
        None,
        None,
        True,
        "scratchterm",
    ),
    scratchgen( # runs command that prints qtile keybindings
        "qtilekeys",
        SCRATCHTERM + " --hold -e /home/rc/mydots/scripts/qtilekeys",
        0.985,
        window_info.calculate_size_percent(1100),
        None,
        None,
        True,
    ),
    scratchgen( # runs command that prints qtile keybindings
        "nvim",
        SCRATCHTERM + "-e nvim",
        0.985,
        window_info.calculate_size_percent(1350),
        None,
        None,
        True,
    ),
    scratchgen(
        "nitrogen",
        "nitrogen",
        0.985,
        window_info.calculate_size_percent(2250),
        None,
        None,
        True,
    ),
    scratchgen(
        "moonlanderlayout",
        "evince /home/rc/documents/hardware/moonlander/MoonlanderLayout6-25-23.pdf",
        # SCRATCHTERM + " --hold -e mupdf /home/rc/documents/hardware/moonlander/MoonlanderLayout6-25-23.pdf",
        0.985,
        window_info.calculate_size_percent(2000),
        None,
        None,
        True,
        # "floating",
    ),
    # scratchgen( # qutebrowser; not working correctly need to difure out the issue 
    #     "qutebrowser",
    #     "qutebrowser",
    #     0.8,
    #     0.8,
    #     None,
    #     None,
    #     False,
    # ),
]

# scratchpad keybindings
spad_keys = [
    Key(
        [SUPER, SHIFT], 'f',
        lazy.group['scratchpad'].dropdown_toggle('term'),
        desc="Launch terminal scratch",
    ),
    Key(
        [SUPER, SHIFT], 'q',
        lazy.group['scratchpad'].dropdown_toggle('qtilekeys'),
        desc="Launch qtile keybindings scratch",
    ),
    Key(
        [SUPER, SHIFT], 'n',
        lazy.group['scratchpad'].dropdown_toggle('nvim'),
        desc="Launch nvim scratch",
    ),
    Key(
        [SUPER, SHIFT], 'w',
        lazy.group['scratchpad'].dropdown_toggle('nitrogen'),
        desc="Launch nitrogen scratch",
    ),
    Key(
        [SUPER, SHIFT], 'z',
        lazy.group['scratchpad'].dropdown_toggle('moonlanderlayout'),
        desc="Launch moonlander layout pdf",
    ),
    # Key(
    #     [SUPER, SHIFT], 't', -- need to figure out issue
    #     lazy.group['scratchpad'].dropdown_toggle('qute'),
    #     desc="Launch qutebrowser",
    # ),
]
