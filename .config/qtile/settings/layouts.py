# bivsk
# https://github.com/bivsk

# Qtile layouts and rules

from libqtile import layout
from libqtile.config import Match
from .theme import colors

layout_conf = {
    'border_focus': colors["focus"][0],
    'border_normal': colors["inactive"][0],
    'border_width': 3,
    'margin': 10
}

layouts = [
    layout.MonadTall(new_client_position="bottom", **layout_conf), # type: ignore
    layout.MonadThreeCol(new_client_position="after_current", **layout_conf), # type: ignore
    layout.Stack(num_stacks=2, **layout_conf), # type: ignore
    layout.VerticalTile(**layout_conf), # type: ignore
    layout.Floating(**layout_conf), # type: ignore
    layout.Max() # type: ignore
]

floating_layout = layout.Floating( # type: ignore
    float_rules=[
        *layout.Floating.default_float_rules, # type: ignore
        Match(title='branchdialog'),
        Match(title='pinentry'),
    ],
    border_focus=colors["color5"][0],
    border_width=3
)
