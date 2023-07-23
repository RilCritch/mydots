#!/usr/bin/env python3


from modules.keys import window_keys, system_keys, app_keys
from modules.groups_q import group_keys
from modules.scratchpads_q import spad_keys


# good start... will use this to create a program for printing my keybindings in a good way

print("window keys:")
for item in window_keys:
    print(f"{item.modifiers} + {item.key} -- {item.desc}")


print()
print("system keys:")
for item in system_keys:
    print(f"{item.modifiers} + {item.key} -- {item.desc}")


print()
print("app keys:")
for item in app_keys:
    print(f"{item.modifiers} + {item.key} -- {item.desc}")


print()
print("group keys:")
for item in group_keys:
    print(f"{item.modifiers} + {item.key} -- {item.desc}")

    
print()
print("spad keys:")
for item in spad_keys:
    print(f"{item.modifiers} + {item.key} -- {item.desc}")
