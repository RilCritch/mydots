# vim:fileencoding=utf-8:foldmethod=marker

from libqtile import layout
from libqtile.config import Match

# temporary variables that I need to move to common file
layout_theme = {
    "margin": 7,
    "border_width": 3,
    "border_focus": "#ecd28b",
    "border_normal": "#0c0e0f",
    "border_on_single": True
    }

# defining layouts that are available on my system - eventually I will create dicts for each layout
base_layouts = [
    # ones i use
    layout.Columns(**layout_theme, insert_position=1), # favorite
    layout.Max(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    # need to look into
    # layout.TreeTab(**layout_theme), # interesting, look into configuration
    # layout.MonadThreeCol(**layout_theme), # great for ultrawide
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
    *layout.Floating.default_float_rules,
    Match(wm_class="confirmreset"),  # gitk
    Match(wm_class="makebranch"),  # gitk
    Match(wm_class="maketag"),  # gitk
    Match(wm_class="ssh-askpass"),  # ssh-askpass
    Match(title="branchdialog"),  # gitk
    Match(title="pinentry"),  # GPG key password entry
    Match(wm_class="floating"),
    
]
