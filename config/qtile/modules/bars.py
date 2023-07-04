# vim:fileencoding=utf-8:foldmethod=marker

from libqtile import bar
from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration, PowerLineDecoration, RectDecoration
from libqtile.lazy import lazy

# defaults
widget_defaults = dict(
    font="JetBrainsMono Nerd Font",
    fontsize=16,
    padding=4,
    foreground='#edeff0',
)

sep_theme = {
    "linewidth": 1,
    "padding": 0,
    "foreground": '#343637',
    # "foreground": ['#e6c465','#ecd28b'],
    "size_percent": 100,
}

powerlinesize = 5

# widgets
def init_top_widgets():
    widgets = [
        widget.Spacer(),
    ]
    return widgets


def init_bot_widgets():
    widgets = [
        widget.Systray(
            icon_size=15,
        ),
        widget.Spacer(),
        # widget.Sep(**sep_theme),
        widget.CapsNumLockIndicator(font='Tinos bold', fontsize=12),
    ]
    return widgets


# top bar
top_widgets = init_top_widgets()
top_bar = bar.Bar(
    top_widgets,
    36,
    background='#0c0e0f',
    opacity=0.8,
    border_width=[3, 0, 3, 0], 
    border_color='#0c0e0f',
)

# bottom bar
bot_widgets = init_bot_widgets()
bot_bar = bar.Bar(
    bot_widgets,
    20,
    background='#0c0e0f',
    opacity=0.80,
)

