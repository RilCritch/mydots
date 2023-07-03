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
        widget.Spacer(length = 6),
        widget.TextBox(
            fmt="󰌠",
            font="Mononoki Nerd Font mono",
            fontsize=42,
            padding=8,
            # foreground=['#4277bd', '#6791C9'],
            background = ['#4277bd', '#6791C9'],
            foreground = '#0c0e0f',
            # foreground=['#e6c465','#ecd28b'],
            mouse_callbacks={
                "Button1": lazy.spawn("rofi -show run"), # eventually change to rofi script that has fave apps
            },
            decorations=[
                PowerLineDecoration(size=powerlinesize),
            ],
        ),
        widget.Spacer(
            length = 1,
            decorations=[
                PowerLineDecoration(size=powerlinesize),
            ],
        ),
        widget.Spacer(length=6, background = "#1f2122"),
        widget.TextBox(
            fmt = "",
            font = "Mononoki Nerd Font mono",
            fontsize = 30,
            foreground = "#ecd28b",
            background = "#1f2122"
        ),
        widget.Clock(
            format="%m/%d/%y ",
            foreground="#edeff0",
            background='#1f2122',
            decorations=[
                PowerLineDecoration(size=powerlinesize),
            ],
        ),
        widget.Spacer(
            length = 1,
            decorations=[
                PowerLineDecoration(size=powerlinesize),
            ],
        ),
        widget.Spacer(length=6, background = "#343637"),
        widget.TextBox(
            fmt = "",
            font = "Mononoki Nerd Font mono",
            fontsize = 30,
            foreground = "#6791c9",
            background = "#343637"
        ),
        widget.Clock(
            format="%I:%M ",
            background='#343637',
            decorations=[
                PowerLineDecoration(size=powerlinesize),
            ],
        ),
        widget.Spacer(
            length = 1,
            decorations=[
                PowerLineDecoration(size=powerlinesize),
            ],
        ),
        widget.Spacer(length=9, background = "#1f2122"),
        widget.TextBox(
            fmt = "󰓃",
            font = "Mononoki Nerd Font mono",
            fontsize = 27,
            foreground = "#78b892",
            background = "#1f2122",
        ),
        widget.Volume(
            background = "#1f2122",
            fmt = "{} ",
            decorations=[
                PowerLineDecoration(size=powerlinesize),
            ],

        ),
        widget.Spacer(
            length = 1,
            decorations=[
                PowerLineDecoration(size=powerlinesize),
            ],
        ),
        widget.Spacer(
            length=3, 
            background = ['#4277bd', '#6791C9'],

            decorations=[
                PowerLineDecoration(size=powerlinesize),
            ],
        ),
        widget.Spacer(
            length = 1,
            decorations=[
                PowerLineDecoration(size=powerlinesize),
            ],
        ),
        # Arrow
        # widget.Spacer(length = 24, background = "#343637"),
        widget.Spacer(length = 24, background = ["#4277bd", "#6791c9"]),
        widget.Spacer(length = 6),
        widget.Spacer(length=1, background = ['#58a779', '#78b892']),
        widget.CurrentLayoutIcon(
            scale=0.85,
            use_mask=True,
            foreground = "#0c0e0f",
            # foreground = ['#4277bd', '#6791C9'],
            # foreground = ['#e6c465','#ecd28b'],
            background = ['#58a779', '#78b892'],
        ),
        widget.Spacer(
            length=1, 
            background = ['#58a779', '#78b892'],
            decorations=[
                PowerLineDecoration(size=powerlinesize),
            ],
        ),
        widget.Spacer(
            length = 1,
            decorations=[
                PowerLineDecoration(size=powerlinesize),
            ],
        ),
        widget.CurrentLayout(
            # background = "#343637",
            background = "#1f2122",
            fmt = " {} ",
            decorations=[
                PowerLineDecoration(size=powerlinesize),
            ],
            fontsize = 14,
        ),
        widget.Spacer(
            length = 1,
            decorations=[
                PowerLineDecoration(size=powerlinesize),
            ],
        ),
        widget.Spacer(
            length=3, 
            background = ['#58a779', '#78b892'],

            decorations=[
                PowerLineDecoration(size=powerlinesize),
            ],
        ),
         widget.Spacer(
            length = 1,
            decorations=[
                PowerLineDecoration(size=powerlinesize),
            ],
        ),
        # Arrow
        # widget.Spacer(length = 12, background = "#1f2122"),
        widget.Spacer(length = 24, background = ['#58a779', '#78b892']),
        widget.Spacer(length = 6),
        # widget.Spacer(length = 6, background = ['#58a779', '#78b892']),
        widget.Spacer(length = 6, background = ['#4277bd', '#6791C9']),
        widget.Spacer(length=6),
        widget.GroupBox(
            highlight_method='block',
            # hide_unused=True,
            highlight_color='#0c0e0f',
            inactive='#484a4b',
            active='#284871',
            font="Mononoki Nerd Font mono",
            block_highlight_text_color='#0c0e0f',
            borderwidth=1,
            # this_current_screen_border=['#4277bd', '#6791C9'],
            # this_current_screen_border=['#e6c465', '#ecd28b'],
            this_current_screen_border=['#58a779', '#78b892'],
            margin_x=0,
            padding_x=6,
            padding_y=-3,
            fontsize=33,
            spacing=4,
            disable_drag = True,
        ),
        widget.Spacer(length=6),
        # widget.Spacer(length = 6, background = "#343637"),
        widget.Spacer(length = 6, background = ['#4277bd', '#6791C9']),
        widget.Spacer(length=6),
        widget.Spacer(
            length = 24, 
            background = ['#58a779', '#78b892'],
            decorations = [
                PowerLineDecoration(path = "arrow_right", size = powerlinesize),
            ],
        ),
        widget.Spacer(
            length=1,
            decorations = [
                PowerLineDecoration(path = "arrow_right", size = powerlinesize),
            ],
        ),
        widget.Spacer(
            length = 3, 
            background = ['#58a779', '#78b892'],
            decorations = [
                PowerLineDecoration(path = "arrow_right", size = powerlinesize),
            ],
        ),
        widget.Spacer(length=6),
        # widget.Sep(**sep_theme),
        widget.TaskList(
            icon_size = 0,
            font = "Tinos bold",
            fontsize=12,
            # foreground = "#edeff0",
            foreground = ['#374041','#505253'],
            borderwidth = 2,
            # border = '#484a4b',
            border = ['#58a779', '#78b892'],
            unfocused_border=['#374041','#505253'],
            margin = 1,
            padding = 10,
            spacing=6,
            # highlight_method = "block",
            title_width_method = "uniform",
            urgent_alert_method = "text",
            urgent_border = '#df5b61',
            rounded = True,
            txt_floating = "",
            txt_maximized = "",
            txt_minimized = "",
            markup_floating="<span foreground='#6791C9'>{}</span>",
            markup_focused="<span foreground='#78b892'>{}</span>",
            markup_maximized="<span foreground='#ecd28b'>{}</span>",
            markup_minimized="<span foreground='#7d7f80' strikethrough='true'>{}</span>",
        ),
        widget.Spacer(length=3),
        widget.Spacer(
            length=1, 
            decorations=[
                PowerLineDecoration(size=powerlinesize),
            ],
        ),
        widget.Spacer(
            length=3, 
            background = ['#58a779', '#78b892'],
            decorations=[
                PowerLineDecoration(size=powerlinesize),
            ],
        ),
        widget.Spacer(
            length=1, 
            decorations=[
                PowerLineDecoration(size=powerlinesize),
            ],
        ),
        widget.Spacer(length = 24, background = ['#58a779', '#78b892']),
        widget.Spacer(length = 6),
        widget.Spacer(length = 6, background = ['#4277bd', '#6791C9']),
        widget.Spacer(length = 6),
        # widget.Spacer(length = 18), # place holder for sys tray
        widget.TextBox(
            fmt = "system info goes here",
        ),
        widget.Spacer(length = 6),
        widget.Spacer(length = 6, background = ['#4277bd', '#6791C9']),
        widget.Spacer(length = 6),
        widget.Spacer(
            length = 24, 
            # background = "#1f2122",
            background = ['#58a779', '#78b892'],
            decorations = [
                PowerLineDecoration(path = "arrow_right", size = powerlinesize),
            ],
        ),
        widget.Spacer(
            length=1, 
            decorations=[
                PowerLineDecoration(path = "arrow_right", size = powerlinesize),
            ],
        ),
        widget.Spacer(
            length = 3,
            background = ['#58a779', '#78b892'],
            decorations=[
                PowerLineDecoration(path = "arrow_right", size = powerlinesize),
            ],
        ),
        widget.Spacer(
            length=1, 
            decorations=[
                PowerLineDecoration(path = "arrow_right", size = powerlinesize),
            ],
        ),
        widget.TextBox(
            fmt = " power ",
            background = "#1f2122",
            decorations=[
                PowerLineDecoration(path = "arrow_right", size = powerlinesize),
            ],
        ),
        widget.Spacer(
            length=1, 
            decorations=[
                PowerLineDecoration(path = "arrow_right", size = powerlinesize),
            ],
        ),
        widget.TextBox(
            fmt = " related ",
            background = "#343637",
            decorations=[
                PowerLineDecoration(path = "arrow_right", size = powerlinesize),
            ],
        ),
        widget.Spacer(
            length=1, 
            decorations=[
                PowerLineDecoration(path = "arrow_right", size = powerlinesize),
            ],
        ),
        widget.TextBox(
            fmt = " shit ",
            background = "#1f2122",
            decorations=[
                PowerLineDecoration(path = "arrow_right", size = powerlinesize),
            ],
        ),
        widget.Spacer(
            length=1, 
            decorations=[
                PowerLineDecoration(path = "arrow_right", size = powerlinesize),
            ],
        ),
        widget.TextBox(
            # fmt = "󰤆",
            fmt = "",
            font = "Mononoki Nerd Font mono",
            fontsize = 42,
            # background = ['#e6c465','#ecd28b'],
            # background = ['#4277bd', '#6791C9'],
            background = ['#58a779', '#78b892'],
            foreground = "#0c0e0f",
            padding = 8,
            mouse_callbacks = {
                "Button1": lazy.spawn("archlinux-logout"), # figure out how to make it floating
            },
        ),
        widget.Spacer(length = 6),
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

