# vim:fileencoding=utf-8:foldmethod=marker

from libqtile import bar
from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration, PowerLineDecoration, RectDecoration
from libqtile.lazy import lazy

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
    "size_percent": 100,
}


# widgets
def init_top_widgets():
    widgets = [
        widget.TextBox(
            fmt=" 󰌠 ",
            fontsize=26,
            padding=0,
            foreground=['#4277bd', '#6791C9'],
            mouse_callbacks={
                "Button1": lazy.spawn("rofi -show run"), # eventually change to rofi script that has fave apps
            },
        ),
        widget.TextBox(
            fmt="Qtile ",
            foreground=['#e6c465','#ecd28b'],
            mouse_callbacks={
                "Button1": lazy.spawn("rofi -show run"), # eventually change to rofi script that has fave apps
            },
        ),
        widget.Clock(
            format=" %m/%d/%y",
            background=['#1f2122'],
            decorations=[
                PowerLineDecoration(path='forward_slash', size=20),
            ],
        ),
        widget.Clock(
            format="%I:%M ",
            background='#343637',
        ),
        widget.Spacer(
            length=6,
        ),
        widget.GroupBox(
            highlight_method='block',
            # hide_unused=True,
            highlight_color='#0c0e0f',
            inactive='#484a4b',
            active='#284871',
            font="Mononoki Nerd Font mono",
            block_highlight_text_color='#0c0e0f',
            borderwidth=1,
            this_current_screen_border=['#4277bd', '#6791C9'],
            margin_x=0,
            padding_x=6,
            padding_y=-3,
            fontsize=33,
            spacing=4,
        ),
        widget.Spacer(
            length=4,
        ),
        widget.TaskList(
            icon_size = 0,
            font = "Tinos Bold",
            fontsize=12,
            foreground = "#edeff0",
            borderwidth = 2,
            border = '#484a4b',
            unfocused_border='#1f2122',
            margin = 0,
            padding = 9,
            spacing=3,
            highlight_method = "block",
            title_width_method = "uniform",
            urgent_alert_method = "text",
            urgent_border = '#df5b61',
            rounded = True,
            txt_floating = "",
            txt_maximized = "",
            txt_minimized = "",
            markup_floating="<span foreground='#6791C9'>{}</span>",
            markup_focused="<span foreground='#ecd28b'>{}</span>",
            markup_maximized="<span foreground='#78b892'>{}</span>",
            markup_minimized="<span foreground='#7d7f80' strikethrough='true'>{}</span>",
        ),
        widget.CurrentLayoutIcon(
            scale=0.90,
            use_mask=True,
            foreground=['#4277bd', '#6791C9'],

        ),
    ]
    return widgets


def init_bot_widgets():
    widgets = [
        widget.Systray(
            icon_size=15,
        ),
        # widget.Sep(**sep_theme),
        # widget.WindowName(
        #     fontsize=12,
        #     empty_group_string="RilCritch's PC",
        #     foreground="#6791C9"
        # ),
        widget.Spacer(),
        # widget.Sep(**sep_theme),
        widget.CapsNumLockIndicator(font='Tinos bold', fontsize=12),
    ]
    return widgets


# top bar
top_widgets = init_top_widgets()
top_bar = bar.Bar(
    top_widgets,
    33,
    background='#0c0e0f',
    opacity=0.80,
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

