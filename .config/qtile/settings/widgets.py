from libqtile import bar, qtile
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration
import platform
from .theme import colors

# Helpers
def dec_group(extrawidth=10):
    return {"decorations": [RectDecoration(colour=colors['darker'], radius=10, extrawidth=extrawidth, filled=True, padding_y=4, group=True)]}

def parse_window_name(text):
    if "Firefox" in text:
        text = text.replace(text, "Firefox")
    elif "Discord" in text:
        text = text.replace(text, "Discord")
    return text

def base(fg='text', bg='dark'): 
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }

def kver():
    return platform.release()

def separator():
    return widget.Sep(**base(), linewidth=0, padding=5)

def icon(fg='text', bg='dark', fontsize=16, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3
    )

def workspaces(groups, fontsize=None, grouppad=10): 
    return [
        widget.TextBox(
            **base(fg='color1'),
            text = "",
            fontsize = 20,
            padding = 20,
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("rofi -show drun -show-icons")},
        ),
        separator(),
        widget.GroupBox(
            **base(fg='light'),
            padding=3,
            fontsize=fontsize,
            active=colors['active'],
            inactive=colors['dark'],
            highlight_method='text',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['focus'],
            disable_drag=True,
            visible_groups=groups,
            **dec_group(grouppad)
        ),
        separator(),
        widget.CurrentLayoutIcon(
            **base(),
            custom_icon_paths = [ "~/.config/qtile/images" ],
            scale = 0.40,
            **dec_group()
        ),
        widget.Spacer(length=bar.STRETCH, **base()),
        widget.WindowName(
            **base(fg='focus'),
            for_current_screen = False,
            parse_text = parse_window_name,
            width = bar.CALCULATED,
        ),
        widget.Spacer(length=bar.STRETCH, **base()),
    ]

# Widget list for primary monitor
primary_widgets = [
    *workspaces([str(i) for i in range(1, 10)]),

    widget.StatusNotifier(
        **base(),
        icon_size = 18,
        highlight_colour = colors["grey"],
        menu_foreground = colors["active"],
        menu_background = colors["grey"],
        menu_border_width = 2,
        padding = 4,
    ),
    separator(),
    widget.TextBox(
        **base(fg='color1'),
        fmt = "  {}",
        text = kver(),
        **dec_group()
    ),

    separator(),
    widget.TextBox(
        **base(fg="color5"),
        text = " ",
        **dec_group()
    ),
    widget.CheckUpdates(
        **base(fg="color5"),
        colour_have_updates=colors["color5"],
        colour_no_updates=colors["dark"],
        no_update_string="0",
        display_format="{updates}",
        distro="Gentoo_eix",
        **dec_group()
    ),
    separator(),
    widget.CryptoTicker(
        **base(fg="color4"),
        crypto = "BTC",
        format = " {symbol} {amount:,.2f}",
        update_interval = 300,
        user_agent = "python-requests/2.31.0",
        symbol = "󰠓",
        **dec_group()
    ),
    separator(),
    widget.Memory(
        **base(fg="color1"),
        fmt = " 󰍛{}",
        format = "{MemUsed: .1f}/{MemTotal:.0f} {mm}",
        measure_mem = "G",
        **dec_group()
    ),
    separator(),
    widget.PulseVolume(
        **base(fg="color3"),
        emoji = True,
        emoji_list = [" 󰖁", " 󰕿", " 󰖀", " 󰕾"],
        limit_max_volume = True,
        **dec_group()
    ),
    separator(),
    widget.TextBox(
        **base(fg="color2"),
        text = " 󰸘",
        **dec_group()
    ),
    widget.Clock(
        **base(fg="color2"),
        format = "%a, %b %d",
        **dec_group()
    ),
    separator(),
    widget.TextBox(
        **base(fg="color6"),
        text = " 󰥔",
        **dec_group()
    ),
    widget.Clock(
        **base(fg="color6"),
        format = "%H:%M",
        **dec_group()
    ),
    separator(),
]

# Widget list for secondary monitor
secondary_widgets = [
    *workspaces(["F5", "F6", "F7", "F8"], 24, 4),

    widget.Mpris2(
        **base(fg="color5"),
        format = "{xesam:artist}: {xesam:title}",
        fmt = " {}",
        paused_text = "  {track}",
        playing_text = "  {track}",
        width = 300,
        **dec_group()
    ),
    separator(),
    widget.PulseVolume(
        **base(fg="color3"),
        emoji = True,
        emoji_list = [" 󰖁", " 󰕿", " 󰖀", " 󰕾"],
        limit_max_volume = True,
        **dec_group()
    ),
    separator(),
    widget.TextBox(
        **base(fg="color2"),
        text = " 󰸘",
        **dec_group()
    ),
    widget.Clock(
        **base(fg="color2"),
        format = "%a, %b %d",
        **dec_group()
    ),
    separator(),
    widget.TextBox(
        **base(fg="color6"),
        text = " 󰥔",
        **dec_group()
    ),
    widget.Clock(
        **base(fg="color6"),
        format = "%H:%M",
        **dec_group()
    ),
    separator(),

]

# Widget list for vertical monitor
vertical_widgets = [
    *workspaces(["F1", "F2", "F3", "F4"], 24, 4),

    widget.PulseVolume(
        **base(fg="color3"),
        emoji = True,
        emoji_list = [" 󰖁", " 󰕿", " 󰖀", " 󰕾"],
        limit_max_volume = True,
        **dec_group()
    ),
    separator(),
    widget.TextBox(
        **base(fg="color6"),
        text = " 󰥔",
        **dec_group()
    ),
    widget.Clock(
        **base(fg="color6"),
        format = "%H:%M",
        **dec_group()
    ),
    separator(),
]

widget_defaults = {
    'font': 'CaskaydiaCove Nerd Font Bold',
    'fontsize': 16,
    'padding': 3,
}
extension_defaults = widget_defaults.copy()
