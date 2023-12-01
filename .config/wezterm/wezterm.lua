-- Pull in the wezterm API
local wezterm = require("wezterm")

-- This table will hold the configuration.
local config = {}

-- In newer versions of wezterm, use the config_builder which will
-- help provide clearer error messages
if wezterm.config_builder then
	config = wezterm.config_builder()
end

-- Colorscheme
--config.color_scheme_dirs = { "~/.config/wezterm/colors" }
config.color_scheme = "Rosé Pine Moon (Gogh)"
config.force_reverse_video_cursor = true

-- Appearance
config.enable_tab_bar = false
-- config.window_background_opacity = 0.99

-- Shell
config.default_prog = { "/usr/local/bin/nu", "-l" }

-- Misc
config.check_for_updates = false
config.hide_mouse_cursor_when_typing = false
config.show_update_window = false
config.window_close_confirmation = "NeverPrompt"

-- Fonts
config.font = wezterm.font("Monaspace Krypton", { weight = "Medium" })
config.font_size = 11.0
config.font_rules = {
	{
		intensity = "Bold",
		italic = true,
		font = wezterm.font({
			family = "Monaspace Radon",
			weight = "Bold",
			style = "Italic",
		}),
	},
	{
		italic = true,
		intensity = "Half",
		font = wezterm.font({
			family = "Monaspace Radon",
			weight = "DemiBold",
			style = "Italic",
		}),
	},
	{
		italic = true,
		intensity = "Normal",
		font = wezterm.font({
			family = "Monaspace Radon",
			weight = "Medium",
			style = "Italic",
		}),
	},
}

return config
