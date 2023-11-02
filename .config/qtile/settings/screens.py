# Multimonitor support

from libqtile.config import Screen
from libqtile import bar
from .widgets import primary_widgets, secondary_widgets, vertical_widgets
from .theme import colors

bar_defaults = {
    "size": 36,
    "border_width": [0, 0, 2, 0],
    "border_color": "#54546d",
    "background_color": colors["dark"],
}

def status_bar(widgets):
    return bar.Bar(widgets, **bar_defaults)

screens = [
    Screen(
        top = status_bar(vertical_widgets),
        wallpaper = "~/.config/qtile/images/wallpaper.png",
        wallpaper_mode = "fill"
    ),
    Screen(
        top = status_bar(primary_widgets),
        wallpaper = "~/.config/qtile/images/wallpaper.png",
        wallpaper_mode = "stretch"
    ),
    Screen(
        top = status_bar(secondary_widgets),
        wallpaper = "~/.config/qtile/images/wallpaper.png",
        wallpaper_mode = "stretch"
    ),
]
