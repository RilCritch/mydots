# vim:fileencoding=utf-8:foldmethod=marker

from libqtile import bar, widget

# defaults
widget_defaults = dict(
    # font="sans",
    font="JetBrainsMono Nerd Font",
    fontsize=14,
    padding=4,
    foreground='#edeff0',
)

sep_theme = {
    "linewidth": 1,
    "padding": 10,
    "foreground": '#505253',
}


# widgets
def init_top_widgets():
    widgets = [
        widget.Volume(
            scroll_delay=0,
        ),   
        widget.Sep(**sep_theme),
        widget.Prompt(),
        widget.WindowName(
            padding=6,
        ),
        widget.Sep(**sep_theme),
        widget.GroupBox(
            highlight_method='line',
            hide_unused=True,
            highlight_color='#343637',
            inactive='#505253',
            active='#edeff0',
            font="JetBrainsMono Nerd Font Bold",
            block_highlight_text_color='#ecd28b',
            borderwidth=0,
            padding=1,
            fontsize=16,
        ),
        widget.Sep(**sep_theme),
        widget.Spacer(),
        widget.Sep(**sep_theme),
        widget.Clock(
            format="%I:%M",
        ),
    ]
    return widgets


def init_bot_widgets():
    widgets = [
        widget.Systray(
            icon_size=15,
        ),
        widget.Spacer(),
        widget.Sep(**sep_theme),
        widget.CapsNumLockIndicator(),
        widget.Sep(**sep_theme),
        widget.Spacer(),
        widget.Sep(**sep_theme),
        widget.CurrentLayout(),
        widget.Sep(**sep_theme),
        widget.CurrentLayoutIcon(),
    ]
    return widgets


# top bar
top_widgets = init_top_widgets()
top_bar = bar.Bar(
    top_widgets,
    30,
    background='#0c0e0f',
    opacity=0.90,
    border_width=[0, 0, 2, 0], 
    border_color='#ecd28b',
)

# bottom bar
bot_widgets = init_bot_widgets()
bot_bar = bar.Bar(
    bot_widgets,
    20,
    background='#0c0e0f',
    opacity=0.90,
)

