# vim:fileencoding=utf-8:foldmethod=marker

from libqtile.config import DropDown, Key, Match
from libqtile.lazy import lazy

from modules.settings import CONTROL, SUPER, SHIFT, TERMINAL, BROWSER
    
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
            match=Match(wm_class=res), # pyright: ignore
            width=w,
            height=h,
            x=x,
            y=y,
            opacity=opacity, # pyright: ignore
            on_focus_lost_hide=autohide, # pyright: ignore
        )
    else:
        spad = DropDown(
            name,
            spawn,
            width=w,
            height=h,
            x=x,
            y=y,
            opacity=opacity, # pyright: ignore
            on_focus_lost_hide=autohide, # pyright: ignore
        )
    return spad

# list of dropdowns
SCRATCHTERM = TERMINAL + " --class=scratchterm"
spads = [
    scratchgen( # basic terminal
        "term",
        SCRATCHTERM,
        0.9,
        window_info.calculate_size_percent(1350),
        None,
        None,
        True,
        "scratchterm",
    ),
    scratchgen( # runs command that prints qtile keybindings
        "qtilekeys",
        SCRATCHTERM + " --hold -e /home/rc/mydots/scripts/qtilekeys",
        0.9,
        window_info.calculate_size_percent(1700),
        None,
        None,
        True,
    ),
    scratchgen( # runs command that prints qtile keybindings
        "term2",
        SCRATCHTERM,
        0.9,
        window_info.calculate_size_percent(1350),
        None,
        None,
        True,
        "scratchterm",
    ),
    scratchgen(
        "cdopen",
        SCRATCHTERM + " -e /home/rc/mydots/scripts/openterm",
        0.9,
        window_info.calculate_size_percent(1800),
        None,
        None,
        True,
    ),
    scratchgen(
        "nitrogen",
        "nitrogen",
        0.9,
        window_info.calculate_size_percent(2250),
        None,
        None,
        True,
    ),
    scratchgen(
        "fzf-run",
        SCRATCHTERM + "--title='Run Programs' --config='/home/rc/mydots/config/kitty/specialconfigs/menu.conf' -e '/home/rc/mydots/scripts/menus/fzf-dmenu.sh'",
        0.375,
        window_info.calculate_size_percent(1150),
        None,
        0.025,
        True,
    ),
    scratchgen(
        "fzf-clip",
        SCRATCHTERM + "--title='Run Programs' --config='/home/rc/mydots/config/kitty/specialconfigs/menu.conf' -e '/home/rc/mydots/scripts/menus/fzf-clip.sh'",
        0.375,
        window_info.calculate_size_percent(1500),
        None,
        0.025,
        True,
    ),
    scratchgen(
        "fzf-sysopts",
        SCRATCHTERM + "--title='Run Programs' --config='/home/rc/mydots/config/kitty/specialconfigs/menu.conf' -e '/home/rc/mydots/scripts/menus/fzf-sysopts-q.sh'",
        0.225,
        window_info.calculate_size_percent(600),
        None,
        0.025,
        True,
    ),
    scratchgen(
        "fzf-powermenu",
        SCRATCHTERM + "--title='Run Programs' --config='/home/rc/mydots/config/kitty/specialconfigs/menu.conf' -e '/home/rc/mydots/scripts/menus/fzf-powermenu-q.sh'",
        0.225,
        window_info.calculate_size_percent(250),
        None,
        0.025,
        True,
    ),
    # scratchgen(
    #     "browser",
    #     "/usr/bin/" + BROWSER,
    #     0.9,
    #     window_info.calculate_size_percent(2250),
    #     None,
    #     None,
    #     True,
    #     "floating",
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
        [SUPER, SHIFT], 'b',
        lazy.group['scratchpad'].dropdown_toggle('qtilekeys'),
        desc="Launch qtile keybindings scratch",
    ),
    Key(
        [SUPER, SHIFT], 'n',
        lazy.group['scratchpad'].dropdown_toggle('term2'),
        desc="Launch secondary terminal scratch",
    ),
    Key(
        [SUPER, SHIFT], 'Return',
        lazy.group['scratchpad'].dropdown_toggle('cdopen'),
        desc="Launch terminal in specified directory",
    ),
    Key(
        [SUPER, SHIFT], 'r',
        lazy.group['scratchpad'].dropdown_toggle('fzf-run'),
        desc="Launch programs",
    ),
    Key(
        [SUPER, SHIFT], 'c',
        lazy.group['scratchpad'].dropdown_toggle('fzf-clip'),
        desc="View clipboard history",
    ),
    Key(
        [SUPER, SHIFT], 's',
        lazy.group['scratchpad'].dropdown_toggle('fzf-sysopts'),
        desc="Select system options",
    ),
    Key(
        [SUPER, CONTROL], 'x',
        lazy.group['scratchpad'].dropdown_toggle('fzf-powermenu'),
        desc="Launch power menu",
    ),
    # Key(
    #     [SUPER, SHIFT], 'w',
    #     lazy.group['scratchpad'].dropdown_toggle('browser'),
    #     desc="Launch browser scratch",
    # ),
    # Key(
    #     [SUPER, SHIFT], 'w',
    #     lazy.group['scratchpad'].dropdown_toggle('nitrogen'),
    #     desc="Launch nitrogen scratch",
    # ),
]
