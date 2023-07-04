# vim:fileencoding=utf-8:foldmethod=marker

from libqtile import bar
from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration, PowerLineDecoration, RectDecoration
from libqtile.lazy import lazy

# colors
colors = { # figure out how to place and set colors from json
    "bg": '#0c0e0f',
    "barbg": ['#6791c944','#0c0e0f66','#0c0e0fbb','#0c0e0f66','#6791c944'],
    # "barbg": '#0c0e0faa',
    "fg": '#edeff0',
    "lightgray": '#7d7f80',
    "gray": '#505253',
    "graygrad": ['#374041','#505253'],
    "darkgray": '#343637',
    "black": '#1f2122',
    "acnt1": '#78b892',
    "acnt1grad": ['#58a779', '#78b892'],
    "acnt2": '#6791c9',
    "acnt2grad": ['#4277bd','#6791c9'],
    "acnt3": '#ecd28b',
    "acnt3grad": ['#e6c465','#ecd28b'],
    "alrt": '#df5b61',
    "alrtgrad": ['#d52a33','#df5b61'],
}

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

icon_defaults = {
    "font": "Mononoki Nerd Font Mono",
}

# widgets
def init_top_widgets():
    widgets = [
        widget.Spacer(),
    ]
    return widgets


def init_bot_widgets():
    widgets = [
        widget.Systray(
            icon_size = 15,
        ),
        widget.Spacer(),
        # widget.Sep(**sep_theme),
        widget.CapsNumLockIndicator(font = 'Tinos bold', fontsize = 12),
    ]
    return widgets


# top bar
top_widgets = init_top_widgets()
top_bar = bar.Bar(
    top_widgets,
    42,
    background = colors["barbg"],
    margin = [9, 6, 0, 6],
    # opacity = 0.8,
    # border_width = [2, 0, 2, 0], 
    border_width = 1,
    # border_color = '#0c0e0f',
    border_color = colors["darkgray"],
)

# bottom bar
bot_widgets = init_bot_widgets()
bot_bar = bar.Bar(
    bot_widgets,
    20,
    background = '#0c0e0f',
    opacity = 0.80,
)

