# vim:fileencoding=utf-8:foldmethod=marker

from libqtile.config import Group, Key
from libqtile.lazy import lazy

from modules.settings import SUPER, SHIFT, CONTROL

# main group info
group_names = [
    "1", # 1 - misc
    "2", # 2 - notes
    "3", # 3 - config editing
    "4", # 4 - config editing
    "5", # 5 - browser
    "6", # 6 - misc terminal
    "7", # 7 - streaming
    "8", # 8 - music
    "9", # 9 - discord
    # "b",
]

group_labels = [
    "", # 1 - misc
    "󰠮", # 2 - notes
    "", # 3 - config editing
    "", # 4 - config editing 
    "󰖟", # 5 - browser
    "", # 6 - misc terminal
    "", # 7 - streaming
    "󰓇", # 8 - music
    "󰙯", # 9 - discord
    # "", # $ - buying stuff
]

group_layouts = [
    "monadthreecol",
    "monadthreecol",
    "monadthreecol",
    "monadthreecol",
    "monadthreecol",
    "monadthreecol",
    "monadthreecol",
    "columns",
    "monadthreecol",
    # "monadthreecol",
]

# set up main group list
main_groups = []
for i in range(len(group_names)):
    main_groups.append(
        Group(
            name = group_names[i],
            layout = group_layouts[i],
            label = group_labels[i],
        )
    )

# set up group keys
group_keys = []
for i in main_groups:
    group_keys.extend(
        [
            Key( # switch to group
                [SUPER],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
                ),
            Key( # move focused window to specified group
                [SUPER, SHIFT],
                i.name,
                lazy.window.togroup(i.name, switch_group=False),
                desc="Switch to & move focused window to group {}".format(i.name),
                ),
            Key( # move focused window to specified group and your focus to that group
                [SUPER, CONTROL],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
                ),
            ]
        )
