# This file is sourced by all *interactive* bash shells on startup,
# including some apparently interactive shells such as scp and rcp
# that can't tolerate any output.  So make sure this doesn't display
# anything or bad things will happen !

# Test for an interactive shell.  There is no need to set anything
# past this point for scp and rcp, and it's important to refrain from
# outputting anything in those cases.
if [[ $- != *i* ]] ; then
	# Shell is non-interactive.  Be done now!
	return
fi

# Source aliases & functions
source ~/.bash_aliases

# No double entries in the shell history.
export HISTCONTROL="$HISTCONTROL erasedups:ignoreboth"

# Do not overwrite files when redirecting output by default.
set -o noclobber

# Set keybinds to vi mode
set -o vi

# Enable doas completion
complete -cf doas

eval "$(starship init bash)"
