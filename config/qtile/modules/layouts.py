# vim:fileencoding=utf-8:foldmethod=marker
import importlib

from libqtile import layout
from libqtile.config import Match, Key
from libqtile.lazy import lazy

# importlib.reload(lazy)

# default layout theme for every layout
layout_theme = {
    "margin": 15,
    "margin_on_single": 20,
    "border_width": 2,
    "border_focus": '#F5C2E7',
    "border_normal": '#313244',
    "border_on_single": True,
}

# specific layout options
columns_opts = {
    "insert_position": 1,
    "num_columns": 3,
}

max_opts = {
    "margin": [15, 1350, 15, 1350],
    "border_width": 3,
    "border_focus": '#7F849C',
    "border_normal": '#313244',
}

three_col_opts = {
    "single_margin": [15, 1350, 15, 1350],
    "ratio": 0.40,
}

floating_opts = {
    "border_focus": '#B4BEFE',
    "border_normal": '#313244',
    "border_width": 2,
    "fullscreen_border_width": 0,
    "max_border_width": 1,
}

# monadtall_opts = {
#
# }
#
# monadwide_opts = {
#
# }

treetab_opts = {
    # sizes
    "font": "JetBrainsMono Nerd Font",
    "fontsize": 13,
    "section_fontsize": 15,
    "font_shadow": None,
    "panel_width": 350,
    # colors
    "active_bg": '#6791C9',
    "active_fg": '#0c0e0f',
    "inactive_bg": '#343637',
    "inactive_fg": '#edeff0',
    "urgent_bg": '#df5b61',
    "urgent_fg": '#edeff0',
    "bg_color": '#0c0e0f',
    "section_fg": '#78b892',
    # sections
    "sections": [
        'Browser',
        'Terminal',
        'Editor',
    ],
    # spacing
    "level_shift": 24, # don't know what it does
    "margin_left": 6, # don't know what it does
    "margin_y": 6, # don't know what it does
    "padding_left": 0,
    "padding_x": 0,
    "padding_y": 4,
    "vspace": 3,
    "section_left": 4,
    "section_padding": 4,
    "section_top": 10,
    # behavior
    "place_right": False,
    "previous_on_rm": True,
}

# defining layouts that are available on my system - eventually I will create dicts for each layout
base_layouts = [
    # ones i use
    layout.MonadThreeCol(**layout_theme, **three_col_opts), # pyright: ignore
    layout.Max(**max_opts), # pyright: ignore
    layout.Columns(**layout_theme, **columns_opts), # pyright: ignore
    layout.MonadTall(**layout_theme), # pyright: ignore
    layout.MonadWide(**layout_theme), # pyright: ignore
    # need to look into
    # layout.TreeTab(**layout_theme, **treetab_opts), # interesting, look into configuration
    # layout.Bsp(**layout_theme), # interesting for ultrawide
    # layout.Stack(**layout_theme), # may find useful for something
    # no use case for/ don't like right now
    # layout.VerticalTile(**layout_theme), # great for vertical monitor - if i end up using one again
    # layout.Tile(**layout_theme), # its okay
    # layout.Spiral(**layout_theme), # dont like it
    # layout.Matrix(**layout_theme), # i dont get it
    # layout.Slice(**layout_theme), # no use case for me
    # layout.RatioTile(**layout_theme), # wouldn't use
    # layout.Floating(**layout_theme), # mid as fuck
    # layout.Zoomy(**layout_theme), # weird but kind of like tabs. Much worse version of treetab
]

# floating layout shit
base_float_rules = [
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules, # pyright: ignore
    Match(wm_class="confirmreset"),  # gitk
    Match(wm_class="makebranch"),  # gitk
    Match(wm_class="maketag"),  # gitk
    Match(wm_class="ssh-askpass"),  # ssh-askpass
    Match(title="branchdialog"),  # gitk
    Match(title="pinentry"),  # GPG key password entry
    Match(wm_class='archlinux-logout'),
    Match(wm_class="floating"),
]
