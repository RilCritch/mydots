# vim:fileencoding=utf-8:foldmethod=marker

from libqtile import layout
from libqtile.config import Match

# temporary variables that I need to move to common file
layout_theme = {
    "margin": 12,
    "border_width": 3,
    "border_focus": "#ecd28b",
    "border_normal": "#0c0e0f"
    }

# defining layouts that are available on my system - eventually I will create dicts for each layout
base_layouts = [
    layout.Columns(**layout_theme), # favorite
    layout.Max(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    ]

# floating layout shit
float_rules = [
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
