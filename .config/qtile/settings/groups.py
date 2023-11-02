# bivsk
# https://github.com/bivsk

# Qtile workspaces

from typing import Callable

from libqtile.core.manager import Qtile
from libqtile.config import DropDown, Group, Key, ScratchPad
from libqtile.command import lazy

from .keys import mod, keys, terminal
if terminal == "footclient": terminal = "foot"

# Primary groups
group_labels = ["一", "二", "三", "四", "五", "六", "七", "八", "九" ]
groups = [Group(f"{i+1}", label=group_labels[i], screen_affinity=1) for i in range(9)]

# Groups for secondary monitors
groups.extend( 
    [
        # Vertical Monitor
        Group(
            name="F1",
            label="󱊫",
            layout="verticaltile",
            screen_affinity=0
        ),
        Group(
            name="F2",
            label="󱊬",
            layout="verticaltile",
            screen_affinity=0
        ),
        Group(
            name="F3",
            label="󱊭",
            layout="verticaltile",
            screen_affinity=0
        ),
        Group(
            name="F4",
            label="󱊮",
            layout="verticaltile",
            screen_affinity=0
        ),

        # Side Monitor
        Group(
            name="F5",
            label="󱊯",
            layout="monadtall",
            screen_affinity=2
        ),
        Group(
            name="F6",
            label="󱊰",
            layout="monadtall",
            screen_affinity=2
        ),
        Group(
            name="F7",
            label="󱊱",
            layout="monadtall",
            screen_affinity=2
        ),
        Group(
            name="F8",
            label="󱊲",
            layout="monadtall",
            screen_affinity=2
        )
    ]
)

# Scratchpads
groups.append(ScratchPad("scratchpad", [
    DropDown("term", terminal, width=0.8, height=0.8, x=0.1, y=0.1, on_focus_lost_hide=False),
    DropDown("term2", terminal, width=0.8, height=0.8, x=0.1, y=0.1, on_focus_lost_hide=False),
    DropDown("neorg", f"{terminal} nvim -c 'Neorg index'", width=0.8, height=0.8, x=0.1, y=0.1, on_focus_lost_hide=False),
    DropDown("files", f"{terminal} nnn", width=0.5, height=0.7, x=0.25, y=0.15, on_focus_lost_hide=False),
    DropDown("voltui", f"{terminal} pulsemixer", width=0.5, height=0.7, x=0.25, y=0.15, on_focus_lost_hide=False),
    DropDown("volgui", "pavucontrol", width=0.5, height=0.7, x=0.25, y=0.15, on_focus_lost_hide=False),
]))

# Track history of focused groups so we can quickly swap to the most recent
# Populate with primary groups to avoid index errors

def go_to_group(name:str) -> Callable:
    def _inner(qtile: Qtile) -> None:
        if len(qtile.screens) == 1:
            qtile.groups_map[name].toscreen()
            return

        if name in ["F1", "F2", "F3", "F4"]:
            qtile.focus_screen(0)
            qtile.groups_map[name].toscreen()
        elif name in ["F5", "F6", "F7", "F8"]:
            qtile.focus_screen(2)
            qtile.groups_map[name].toscreen()
        else:
            qtile.focus_screen(1)
            qtile.groups_map[name].toscreen()

    return _inner


# Slice to ignore scratchpad group
for group in groups[:-1]:
    keys.extend(
        [
            # mod + group number = switch to group
            Key([mod], group.name, lazy.function(go_to_group(group.name))),

            # mod + shift + group number = move focused client to group
            Key(
                [mod, "shift"],
                group.name,
                lazy.window.togroup(group.name, switch_group=False),
                desc = f"Move focused client to group {group.name}",
            ),
        ]
    )

# Toggle last focused group
keys.append(Key([mod], "Tab", lazy.screen.toggle_group()))
keys.append(Key([mod], "grave", lazy.group["scratchpad"].dropdown_toggle('term')))
keys.append(Key([mod, "shift"], "grave", lazy.group["scratchpad"].dropdown_toggle('term2')))
keys.append(Key([mod], "n", lazy.group["scratchpad"].dropdown_toggle('neorg')))
keys.append(Key([mod], "v", lazy.group["scratchpad"].dropdown_toggle('voltui')))
keys.append(Key([mod, "shift"], "v", lazy.group["scratchpad"].dropdown_toggle('volgui')))
keys.append(Key([mod], "e", lazy.group["scratchpad"].dropdown_toggle('files')))
