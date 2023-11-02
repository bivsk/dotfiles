# /etc/skel/.bash_profile

# This file is sourced by bash for login shells.  The following line
# runs your .bashrc and is recommended by the bash info pages.
if [[ -f ~/.bashrc ]] ; then
	. ~/.bashrc
fi

# Wayland support for Qt applications
export QT_QPA_PLATFORM=wayland

export MANPAGER="sh -c 'col -bx | bat -l man -p'"
export PASSWORD_STORE_DIR="$HOME/.local/share/password-store"
export XDG_DATA_DIRS="$XDG_DATA_DIRS:$HOME/.local/share"
export PATH="$HOME/.local/bin:$PATH"
