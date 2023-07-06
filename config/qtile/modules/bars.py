# vim:fileencoding=utf-8:foldmethod=marker

from libqtile import bar
from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration, PowerLineDecoration, RectDecoration
from libqtile.lazy import lazy

# colors
colors = { # figure out how to place and set colors from json
    "bg": '#0c0e0f',
    # "barbg": '#0c0e0f9f', # blk
    # "barbg": '#6791c930', # blu
    "barbg": '#1f212296', # gry
    # "barbg": '#78b89239', # grn
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
    "transparent": "#00000000"
}

# defaults
widget_defaults = dict(
    font = "JetBrainsMono Nerd Font",
    fontsize = 16,
    padding = 7,
    foreground = colors["fg"],
)

sep_theme = { # section seperator
    "size_percent": 100,
    "foreground": colors["bg"],
    "background": colors["bg"],
    "linewidth": 0,
    "padding": 5,
}

mini_sep = { # sep for within section
    "size_percent": 60,
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
            fontsize = 48,
            # background = colors["acnt2grad"],
            foreground = colors["acnt1grad"],
            padding = 10,
            mouse_callbacks = {
                "Button1": lazy.spawn("rofi -show run"), # eventually change to rofi script that has fave apps
                "Button3": lazy.spawn("archlinux-logout"), # figure out how to make it floating
            },
        ),
        # end of python logo
        widget.Sep(**sep_theme), 
        # date
        widget.TextBox( # date icon
            **icon_defaults,
            fmt = "󰸘",
            foreground = colors["acnt3grad"],
            padding = 10,
            # mouse_callbacks = {}, # add mouse callback to open calender 
        ),
        widget.Clock( # date
            format = "%m/%d/%y",
            foreground = colors["acnt3grad"],
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
            foreground = colors["acnt2grad"],
            padding = 10,
            # mouse_callbacks = {}, # add mouse callback to open up alarm/timer
        ),
        widget.Clock( # time
            format = "%I:%M:%S",
            foreground = colors["acnt2grad"],
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
            foreground = colors["acnt1grad"],
            padding = 10,
            # mouse_callbacks = {}, # add mouse callback to open volume control
        ),
        widget.Volume(
            foreground = colors["acnt1grad"],
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
            border = colors["acnt1"] + "39",
            foreground = colors["fg"] + "cc",
            margin_x = -3,
            margin_y = -1,
            padding_x = 20,
            padding_y = 12,
            txt_floating = "󰀜 ",
            txt_maximized = "󰊓 ",
            txt_minimized = "󱞞 ",
        ),
        
        # right side of bar ------------------------------------------------------------------------------ #
        widget.Sep(**sep_theme),
        # groups
        widget.GroupBox(
            font = "Mononoki Nerd Font Mono",
            fontsize = 40,
            highlight_method = "block",
            urgent_alert_method = "block",
            # background = colors["black"],
            block_highlight_text_color = colors["bg"],
            # this_current_screen_border = colors["acnt1grad"],
            this_current_screen_border = colors["acnt1"] + "c5",
            active = colors["acnt2"] + "88",
            inactive = colors["darkgray"],
            margin_x = 0,
            margin_y = 3,
            padding_x = 6,
            padding_y = -3,
            spacing = 3,
            disable_drag = True,
        ),
        # end of groups
        widget.Sep(**sep_theme),
        # layout
        widget.CurrentLayout(
            fontsize = 14,
            # background = colors["black"],
            foreground = colors["acnt1grad"],
            padding = 10,
        ),
        widget.Sep(**mini_sep),
        widget.Spacer(length = 10),
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
    background = colors["barbg"],
    margin = [9, 6, 0, 6],
)

# bottom bar
bot_widgets = init_bot_widgets()
bot_bar = bar.Bar(
    bot_widgets,
    20,
    background = colors["bg"],
    opacity = 0.80,
)

