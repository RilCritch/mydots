# vim:fileencoding=utf-8:foldmethod=marker

# Variables
# keys
SUPER = "mod4"
SHIFT = "shift"
ALT = "mod1"
CONTROL = "control"

# applications
TERMINAL = "kitty"
BROWSER = "firefox"
EDITOR = "kitty -e nvim"

# qtile configuration options {{{

# If a window requests to be fullscreen, it is automatically fullscreened.
# Set this to false if you only want windows to be fullscreen if you ask them to be.
auto_fullscreen = True

# If things like steam games want to auto-minimize themselves when losing focus, should we respect this or not?
auto_minimize = True

# When clicked, should the window be brought to the front or not. 
# If this is set to "floating_only", only floating windows will get affected (This sets the X Stack Mode to Above.)
bring_front_click = False

# If true, the cursor follows the focus as directed by the keyboard, 
# warping to the center of the focused window. 
# When switching focus between screens, If there are no windows in the screen, 
# the cursor will warp to the center of the screen.
cursor_warp = False

# A function which generates group binding hotkeys. 
# It takes a single argument, the DGroups object, 
# and can use that to set up dynamic key bindings.
dgroups_key_binder = None

# A list of Rule objects which can send windows to various groups based on matching criteria.
dgroups_app_rules = []  # type: list

# Behavior of the _NET_ACTIVATE_WINDOW message sent by applications
    # urgent: urgent flag is set for the window
    # focus: automatically focus the window
    # smart: automatically focus if the window is in the current group
    # never: never automatically focus any window that requests it
focus_on_window_activation = "smart"

# Controls whether or not focus follows the mouse around as it moves across windows in a layout.
follow_mouse_focus = False

# Controls whether or not to automatically reconfigure screens when there are changes in randr output configuration.
reconfigure_screens = True

# Gasp! We're lying here. In fact, nobody really uses or cares about this string besides java UI toolkits; 
# you can see several discussions on the mailing lists, GitHub issues, 
# and other WM documentation that suggest setting this string if your java app doesn't work correctly. 
# We may as well just lie and say that we're a working one by default. 
# We choose LG3D to maximize irony: 
# it is a 3D non-reparenting WM written in java that happens to be on java's whitelist.
wmname = "qtile"

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None
# }}}
