# vim:fileencoding=utf-8:foldmethod=marker

from libqtile.config import Group, Key
from libqtile.lazy import lazy

from settings import SUPER, SHIFT

# main group info
group_names = [
    "1", # 1 - misc stuff
    "2", # 2 - misc stuff
    "3", # 3 - misc stuff
    "4", # 4 - browser 
    "5", # 5 - wm config
    "6", # 6 - nvim config
    "7", # 7 - coding
    "8", # 8 - music
    "9", # 9 - discord
]

group_labels = [
    "󰛨", # 1 - misc/random research
    "󰠮", # 2 - notes
    "", # 3 - config editing
    "", # 4 - config editing 
    "󰖟", # 5 - browser
    "", # 6 - terminal
    "", # 7 - streaming
    "󰓇", # 8 - music
    "󰙯", # 9 - discord
]

group_layouts = [
    "columns", # 1 - misc stuff 
    "columns", # 2 - misc stuff
    "columns", # 3 - misc stuff
    "columns", # 4 - browser 
    "columns", # 5 - qtile config
    "columns", # 6 - nvim config
    "columns", # 7 - coding
    "columns", # 8 - music
    "max", # 9 - discord
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
            # mod1 + letter of group = switch to group
            Key(
                [SUPER],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
                ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [SUPER, SHIFT],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
                ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
            ]
        )
