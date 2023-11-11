# bivsk
# https://github.com/bivsk

# Qtile keybindings

from libqtile.config import Key
from libqtile.lazy import lazy

from fake_fullscreen import toggle_fullscreen_state

mod = "mod4"
terminal = "footclient"

keys = [Key(key[0], key[1], *key[2:]) for key in [
    # ---------------- Windows ----------------

    # Switch windows focus
    ([mod], "j", lazy.layout.down()),
    ([mod], "k", lazy.layout.up()),
    ([mod], "h", lazy.layout.left()),
    ([mod], "l", lazy.layout.right()),

    # Change window sizes (MonadTall)
    ([mod, "shift"], "l", lazy.layout.grow()),
    ([mod, "shift"], "h", lazy.layout.shrink()),

    # Toggle fullscreen
    ([mod], "f", lazy.window.toggle_fullscreen()),
    ([mod, "shift"], "f", lazy.function(toggle_fullscreen_state)),

    # Toggle floating
    ([mod], "t", lazy.window.toggle_floating()),

    # Move windows up or down in current stack
    ([mod, "shift"], "j", lazy.layout.shuffle_down()),
    ([mod, "shift"], "k", lazy.layout.shuffle_up()),

    # Switch focus between stacks
    ([mod], "l", lazy.layout.next()),
    ([mod], "h", lazy.layout.previous()),

    # Move windows between stacks
    ([mod, "shift"], "n", lazy.layout.client_to_next()),
    ([mod, "shift"], "p", lazy.layout.client_to_previous()),

    # Toggle split on stack layout
    ([mod, "shift"], "s", lazy.layout.toggle_split()),

    # Toggle between different layouts
    ([mod, "shift"], "Tab", lazy.next_layout()),

    # Kill window
    ([mod, "shift"], "c", lazy.window.kill()),

    # Switch focus of monitors
    ([mod], "period", lazy.next_screen()),
    ([mod], "comma", lazy.prev_screen()),

    # Restart Qtile
    ([mod, "control"], "r", lazy.reload_config()),
    ([mod, "control"], "q", lazy.shutdown()),

    # ------------------ Apps -----------------

    # Menu
    ([mod], "p", lazy.spawn("rofi -show drun")),

    # Terminal
    ([mod, "shift"], "Return", lazy.spawn(terminal)),

    # Notification center
    ([mod], "backslash", lazy.spawn("swaync-client -t")),

    # Dmenu
    ([mod, "shift"], "s", lazy.spawn("dm-position-size")),

    # ----------------- Media -----------------

    # Volume
    ([], "XF86AudioRaiseVolume", lazy.spawn("wpctl set-volume @DEFAULT_AUDIO_SINK@ 2%+")),
    ([], "XF86AudioLowerVolume", lazy.spawn("wpctl set-volume @DEFAULT_AUDIO_SINK@ 2%-")),
    ([], "XF86AudioMute", lazy.spawn("wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle")),

    # Media
    ([], "XF86AudioNext", lazy.spawn("playerctl --all-players next")),
    ([], "XF86AudioPrev", lazy.spawn("playerctl --all-players previous")),
    ([], "XF86AudioPlay", lazy.spawn("playerctl --all-players play-pause")),

    # Widget
    ([mod], "a", lazy.widget["mpris2"].toggle_player()),
]]            
              
              
