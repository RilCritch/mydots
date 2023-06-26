from screeninfo import get_monitors


# convert pixel size to a percentage of current screen
def calculate_size_percent(size=None):
    size_percent = 0.5
    monitor_width = get_monitors()[0].width

    if size is None:
        return size_percent

    if size > 0 and size < monitor_width:
        size_percent = size/monitor_width
    elif size >= monitor_width:
        size_percent = 1

    return size_percent
