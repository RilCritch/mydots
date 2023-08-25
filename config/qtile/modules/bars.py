# vim:fileencoding=utf-8:foldmethod=marker

from libqtile import bar
from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration, PowerLineDecoration, RectDecoration
from libqtile.lazy import lazy

# yoru = { # figure out how to place and set colors from json
#     "bg": '#0c0e0f',
#     "barbg": '#343637a3',
#     "fg": '#edeff0',
#     "lightgray": '#7d7f80',
#     "gray": '#505253',
#     "graygrad": ['#374041','#505253'],
#     "darkgray": '#343637',
#     "black": '#1f2122',
#     "acnt1": '#78b892',
#     "acnt1grad": ['#58a779', '#78b892'],
#     "acnt2": '#6791c9',
#     "acnt2grad": ['#4277bd','#6791c9'],
#     "acnt3": '#ecd28b',
#     "acnt3grad": ['#e6c465','#ecd28b'],
#     "alrt": '#df5b61',
#     "alrtgrad": ['#d52a33','#df5b61'],
#     "transparent": "#fefefe00"
# }

# colors
# catppuccin-mocha
colors = { # figure out how to place and set colors from json
    "bg": '#11111b',
    "barbg": '#313244a3',
    "fg": '#cdd6f4',
    "lightgray": '#7f849c',
    "gray": '#585b70',
    "graygrad": ['#313244','#585b70'],
    "darkgray": '#313244',
    "black": '#181825',
    "acnt2": '#f5c2e7',
    "acnt2grad": ['#ed91d5', '#f5c2e7'],
    "acnt1": '#89b4fa',
    "acnt1grad": ['#6ca2f9','#89b4fa'],
    "acnt3": '#94e2d5',
    "acnt3grad": ['#4bceb8','#94e2d5'],
    "alrt": '#f38ba8',
    "alrtgrad": ['#ec4675','#f38ba8'],
    "transparent": "#fefefe00"
}

# defaults
widget_defaults = dict(
    font = "JetBrainsMono Nerd Font",
    fontsize = 16,
    padding = 7,
    foreground = colors["fg"],
    background = colors["barbg"],
)

sep_theme = { # section seperator
    "size_percent": 100,
    "foreground": colors["bg"],
    "background": colors["transparent"],
    "linewidth": 0,
    "padding": 6,
}

mini_sep = { # sep for within section
    "size_percent": 50,
    "foreground": colors["gray"],
    # "background": colors["black"],
    "linewidth": 2,
    "padding": 3,
}

spacer_theme = {
    "length": 10,
}

icon_defaults = {
    "font": "Mononoki Nerd Font Mono",
    "fontsize": 30,
}

# widgets
def init_top_widgets():
    widgets = [
        # right side of bar ------------------------------------------------------------------------------ #
        # python logo that runs rofi and logout script
        widget.TextBox( # ** maybe change to image and use mask
            font = "Mononoki Nerd Font Mono",
            fmt = "󰌠",
            fontsize = 51,
            background = colors["acnt1grad"],
            foreground = colors["black"],
            padding = 10,
            mouse_callbacks = {
                "Button1": lazy.spawn("rofi -show run"), # eventually change to rofi script that has fave apps
                "Button3": lazy.spawn("/home/rc/mydots/scripts/rofiscripts/powermenu.sh"), # figure out how to make it floating
            },
        ),
        # end of python logo
        widget.Sep(**sep_theme), 
        # date
        widget.TextBox( # date icon
            **icon_defaults,
            fmt = "󰸘",
            foreground = colors["acnt2"],
            padding = 10,
            # mouse_callbacks = {}, # add mouse callback to open calender 
        ),
        widget.Clock( # date
            format = "%m/%d/%y",
            foreground = colors["acnt2"],
            padding = 0,
            # mouse_callbacks = {}, # add mouse callback to open calender 
        ),
        # end of date
        widget.Spacer(**spacer_theme), 
        widget.Sep(**mini_sep),
        # time
        widget.TextBox( # time icon
            **icon_defaults,
            fmt = "",
            foreground = colors["acnt1"],
            padding = 10,
            # mouse_callbacks = {}, # add mouse callback to open up alarm/timer
        ),
        widget.Clock( # time
            format = "%I:%M:%S",
            foreground = colors["acnt1"],
            padding = 0,
            # mouse_callbacks = {}, # add mouse callback to open up alarm/timer
        ),
        # end of time
        widget.Spacer(**spacer_theme),
        widget.Sep(**mini_sep),
        # volume
        widget.TextBox(
            **icon_defaults,
            fmt = "󰓃",
            foreground = colors["acnt2"],
            padding = 10,
            # mouse_callbacks = {}, # add mouse callback to open volume control
        ),
        widget.Volume(
            foreground = colors["acnt2"],
            padding = 0,
            scrool_delay = 0,
        ),
        # end of volume
        widget.Spacer(**spacer_theme),
        widget.Sep(**sep_theme),

        # center of bar ---------------------------------------------------------------------------------- #
        widget.TaskList(
            highlight_method = "block",
            title_width_method = "uniform",
            rounded = False,
            icon_size = 0,
            borderwidth = 0,
            background = colors["transparent"],
            border = colors["lightgray"] + "79",
            unfocused_border = colors["barbg"],
            foreground = colors["fg"] + "cc",
            margin_x = 0,
            margin_y = -1,
            padding_x = 12,
            padding_y = 12,
            spacing = 6,
            txt_floating = "󰀜 ",
            txt_maximized = "󰊓 ",
            txt_minimized = "󱞞 ",
            markup_minimized="<span strikethrough='true'>󱞞 {}</span>",
        ),

        # right side of bar ------------------------------------------------------------------------------ #
        widget.Sep(**sep_theme),
        # groups
        widget.GroupBox(
            font = "Mononoki Nerd Font Mono",
            fontsize = 40,
            highlight_method = "block",
            urgent_alert_method = "block",
            block_highlight_text_color = colors["bg"] + "c5",
            this_current_screen_border = colors["acnt2"] + "c5",
            active = colors["acnt2"] + "c5",
            inactive = colors["gray"] + "8a",
            margin_x = 0,
            margin_y = 3,
            padding_x = 6,
            padding_y = -3,
            spacing = 3,
            disable_drag = True,
        ),
        # end of groups
        widget.Sep(**sep_theme),
        widget.CurrentLayoutIcon( # layout icon
            use_mask = True,
            # background = colors["black"],
            foreground = colors["acnt1grad"],
            # background = colors["acnt2grad"],
            # foreground = colors["black"],
            scale = 1,
            padding = 0,
        ),
        # end of layout
    ]
    return widgets


def init_bot_widgets():
    widgets = [
        widget.Systray(
            icon_size = 15,
        ),
        widget.Spacer(),
        widget.CapsNumLockIndicator(fontsize = 12),
    ]
    return widgets


# top bar
top_widgets = init_top_widgets()
top_bar = bar.Bar(
    top_widgets,
    42,
    background = colors["transparent"],
    margin = [9, 9, 0, 9],
)

# bottom bar
bot_widgets = init_bot_widgets()
bot_bar = bar.Bar(
    bot_widgets,
    20,
    background = colors["bg"],
)

