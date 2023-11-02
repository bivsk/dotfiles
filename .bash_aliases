# bash aliases and functions
# bivsk (four@gentoo)

# General
alias ..="cd .."
alias ...="cd ../.."
alias c="clear"
alias vim="/usr/bin/nvim"
alias vi="/usr/bin/nvim"
alias cat="/usr/bin/bat"
alias duf="/usr/bin/duf --hide special"

# Start Qtile (wayland)
alias startqtile="/usr/bin/dbus-launch --exit-with-session /usr/bin/qtile start -b wayland"

# Privilege escalation with doas
alias reboot="/usr/bin/doas /sbin/reboot"
alias shutdown="/usr/bin/doas /sbin/shutdown"

# Misc
alias moe="/usr/bin/mpv https://listen.moe/stream"
alias neo="/usr/bin/neo --defaultbg"

# qlop
alias ql="/usr/bin/qlop -r"
alias qla="/usr/bin/qlop -a"

# Git
alias gs="/usr/bin/git status"
alias gb="/usr/bin/git branch"
alias gl="/usr/bin/git log"
alias gch="/usr/bin/git checkout"
alias dots="/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME"

# eza (ls)
alias ls="/usr/bin/eza --icons"
alias l="/usr/bin/eza --icons"
alias la="/usr/bin/eza -a --icons"
alias ll="/usr/bin/eza --all --header --long --group --icons --git"
alias lt="/usr/bin/eza --tree --level 3 --icons"
alias llt="/usr/bin/eza --long --tree --level 3 --icons --git"

# Eix
alias unstable-world="/usr/bin/eix -# --world --installed-unstable --not -O"

# Output package ebuilds.
qebuild() { /usr/bin/equery which -e "$1" | /usr/bin/bat -l ebuild; }
