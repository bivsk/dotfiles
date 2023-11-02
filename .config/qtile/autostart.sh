#!/bin/sh

# Desktop portal
/usr/libexec/xdg-desktop-portal -r &

# Notifcation daemon
swaync &

# Configure displays
kanshi &

# Start pipewire
gentoo-pipewire-launcher &

# Start foot server
foot --server &

# Red light
sleep 2
wlsunset -t 3500 -T 5700 -l 40 -L -75.2 &
